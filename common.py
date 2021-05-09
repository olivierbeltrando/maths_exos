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
        self.previous = None
        self.streak = 0
        self.longest_streak = 0


class Operation(Enum):
    def __init__(self, _):
        self.success = None

    Add = auto()
    Sub = auto()
    Mult = auto()
    Div = auto()
    Compl = auto()

    @classmethod
    def random(cls):
        possible_operations = [
            cls.Add,
            cls.Sub,
            cls.Sub,
            cls.Div,
            cls.Compl,
        ]
        return possible_operations[randint(0, len(possible_operations) - 1)]

    def __repr__(self):
        if self == Operation.Add:
            return "+"
        if self == Operation.Sub:
            return "-"
        if self == Operation.Mult:
            return "x"
        if self == Operation.Div:
            return "/"
        if self == Operation.Compl:
            return "complement à"
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
        if self == Operation.Compl:
            return j - i
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
        if status.previous is not None:
            if status.previous.success:
                print(
                    f"{Bcolors.HEADER}Bien joué :){Bcolors.ENDC} tu en as fait {status.streak} sans faire de fautes"
                )
            else:
                print(f"{Bcolors.FAIL}Arf dommage :({Bcolors.ENDC}")
        else:
            print("Exercice-time :)")

        print(
            f"Record sans fautes: {Bcolors.HEADER}{status.longest_streak}{Bcolors.ENDC}"
        )
        print(f"Opérations réussies: {Bcolors.HEADER}{len(status.dones)}{Bcolors.ENDC}")
        print(f"Opérations à faire: {Bcolors.OKBLUE}{len(status.to_do)}{Bcolors.ENDC}")
        print(
            f"Opérations à re-faire: {Bcolors.FAIL}{len(status.failed)}{Bcolors.ENDC}"
        )
        txt = f"{i} {repr(operation)} {j} ="
        print(txt)
        try:
            res = input()
            res = int(res.strip())
        except ValueError:
            print("ce n'est pas un nombre...")
            continue
        except KeyboardInterrupt as e:
            yn = input("abandon ?\n")
            if yn.lower() in ["y", "oui", "yes"]:
                raise e
            continue

        expected = operation.compute(i, j)
        success = res == expected

        operation.success = success
        status.previous = operation
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
    interrupted = False
    try:
        while status.to_do or status.failed:
            if to_do:
                ele = to_do.pop()
            elif status.failed:
                ele = status.failed.pop()
            res = exo(*ele, status)
            if res == "success":
                status.streak += 1
                if status.longest_streak < status.streak:
                    status.longest_streak = status.streak
                status.cpt_good += 1
                status.dones.append(ele)
            else:
                status.streak = 0
                status.difficults.add(ele)
                status.cpt_bad += 1
                # errors are added twice
                status.failed.append(ele)
                # except for '-' or Compl
                i, j, operation = ele
                if operation not in (Operation.Sub, Operation.Compl):
                    status.failed.append((j, i, operation))
                shuffle(status.failed)
    except KeyboardInterrupt:
        interrupted = True
        print("Programme interrompu")
        restant = len(status.to_do) + len(status.failed)
        print(f"Il restait à faire: {Bcolors.FAIL}{restant}{Bcolors.ENDC}")

    if not interrupted:
        print(f"{Bcolors.HEADER}BRAVO c'est terminé {Bcolors.ENDC}")
    print(f"Tu as fait {Bcolors.HEADER}{len(status.dones)}{Bcolors.ENDC} opérations")
    print(f"Fautes: {Bcolors.FAIL}{status.cpt_bad}{Bcolors.ENDC}")
    print(f"Difficiles: {Bcolors.FAIL}{status.difficults}{Bcolors.ENDC}")
    seconds = [t.total_seconds() for t in status.temps]
    somme = int(sum(seconds))
    if len(seconds) != 0:
        average = int(sum(seconds) / len(seconds))
        print(f"Tu as mis {somme}s soit {average}s par réponse")
