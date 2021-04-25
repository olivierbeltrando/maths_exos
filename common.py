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


class Op(Enum):
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
        if self == Op.Add:
            return "+"
        if self == Op.Sub:
            return "-"
        if self == Op.Mult:
            return "x"
        if self == Op.Div:
            return "/"
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
        print(
            f"Multiplications réussies: {Bcolors.HEADER}{len(status.dones)}{Bcolors.ENDC}"
        )
        print(
            f"Multiplications a faire: {Bcolors.OKBLUE}{len(status.to_do)}{Bcolors.ENDC}"
        )
        print(
            f"Multiplications a re-faire: {Bcolors.FAIL}{len(status.failed)}{Bcolors.ENDC}"
        )
        txt = f"{i} {repr(operation)} {j} ="
        print(txt)
        if operation == operation.Add:
            expected = i + j
        elif operation == operation.Sub:
            expected = i - j
        elif operation == operation.Mult:
            expected = i * j
        elif operation == operation.Div:
            expected = i / j
        res = input()
        try:
            res = int(res.strip())
        except ValueError:
            print("ce n'est pas un nombre...")
            continue

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
            if operation != Op.Sub:
                status.failed.append((j, i, operation))
            shuffle(status.failed)

    print(f"{Bcolors.HEADER}BRAVO c'est terminé {Bcolors.ENDC}")
    print(
        f"Tu as fait {Bcolors.HEADER}{len(status.dones)}{Bcolors.ENDC} multiplications"
    )
    print(f"Fautes: {Bcolors.FAIL}{status.cpt_bad}{Bcolors.ENDC}")
    print(f"Difficiles: {Bcolors.FAIL}{status.difficults}{Bcolors.ENDC}")
    seconds = [t.total_seconds() for t in status.temps]
    somme = int(sum(seconds))
    average = int(sum(seconds) / len(seconds))
    print(f"Tu as mis {somme}s soit {average}s par réponse")
