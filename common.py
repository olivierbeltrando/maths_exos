import os

from datetime import datetime
from enum import Enum, auto
from random import randint, shuffle


class Status:
    def __init__(self, to_do):
        self.to_do = to_do
        self.dones = []
        self.failed = []
        self.cpt_good = 0
        self.cpt_bad = 0
        self.difficults = set()
        self.temps = []


class Operation(Enum):
    Add = auto()
    Sub = auto()
    Mult = auto()
    Div = auto()

    @classmethod
    def random(cls):
        return {
            0: cls.Add,
            1: cls.Sub,
            2: cls.Sub,
            3: cls.Div,
        }[randint(0, 3)]

    def __repr__(self):
        if self == Operation.Add:
            return "+"
        if self == Operation.Sub:
            return "-"
        if self == Operation.Mult:
            return "x"
        if self == Operation.Div:
            return "/"
        raise Exception("should never occur")

    def compute(self, i, j):
        if self == Operation.Add:
            return i + j
        if self == Operation.Sub:
            return i - j
        if self == Operation.Mult:
            return i * j
        if self == Operation.Div:
            return i / j
        raise Exception("should never occur")


class Bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def exo(i, j, operation, status):
    start_t = datetime.now()
    while True:
        os.system("clear")
        print(f"Opérations réussies: {Bcolors.HEADER}{len(status.dones)}{Bcolors.ENDC}")
        print(f"Opérations à faire: {Bcolors.OKBLUE}{len(status.to_do)}{Bcolors.ENDC}")
        print(
            f"Opérations à re-faire: {Bcolors.FAIL}{len(status.failed)}{Bcolors.ENDC}"
        )
        txt = f"{i} {repr(operation)} {j} ="
        print(txt)
        res = input()
        try:
            res = int(res.strip())
        except ValueError:
            print("ce n'est pas un nombre...")
            continue

        expected = operation.compute(i, j)
        success = res == expected
        print(f"{txt} {expected}")
        if success:
            print(f"{Bcolors.HEADER}bravo{Bcolors.ENDC}\n")
            end_t = datetime.now()
            status.temps.append(end_t - start_t)
            return "success"
        print(f"{Bcolors.FAIL}dommage{Bcolors.ENDC}\n")
        return "failure"


def do_exercise(to_do):
    # type "set" is not really ranmdom. shuffle ftw
    shuffle(to_do)
    status = Status(to_do)

    while status.to_do or status.failed:
        if to_do:
            ele = to_do.pop()
        elif status.failed:
            ele = status.failed.pop()
        res = exo(*ele, status)
        if res == "success":
            status.cpt_good += 1
            status.dones.append(ele)
        else:
            status.difficults.add(ele)
            status.cpt_bad += 1
            # errors are added twice
            status.failed.append(ele)
            # except for '-'
            i, j, operation = ele
            if operation != Operation.Sub:
                status.failed.append((j, i, operation))
            shuffle(status.failed)

    print(f"{Bcolors.HEADER}BRAVO c'est terminé {Bcolors.ENDC}")
    print(f"Tu as fait {Bcolors.HEADER}{len(status.dones)}{Bcolors.ENDC} opérations")
    print(f"Fautes: {Bcolors.FAIL}{status.cpt_bad}{Bcolors.ENDC}")
    print(f"Difficiles: {Bcolors.FAIL}{status.difficults}{Bcolors.ENDC}")
    seconds = [t.total_seconds() for t in status.temps]
    somme = int(sum(seconds))
    average = int(sum(seconds) / len(seconds))
    print(f"Tu as mis {somme}s soit {average}s par réponse")
