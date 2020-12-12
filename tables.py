import os
import sys

from datetime import datetime
from random import shuffle

to_do = []
dones = []
failed = []
cpt_good = 0
cpt_bad = 0
difficults = set()

tables = sys.argv[1:]
print(f"revisions pour les tables de {tables}")
for i in tables:
    for j in range(11):
        to_do.append((int(i), j))

# type "set" is not really ranmdom. shuffle ftw
shuffle(to_do)


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


temps = []


def exo(i, j):
    start_t = datetime.now()
    while True:
        os.system("clear")
        print(f"Multiplications réussies: {bcolors.HEADER}{len(dones)}{bcolors.ENDC}")
        print(f"Multiplications a faire: {bcolors.OKBLUE}{len(to_do)}{bcolors.ENDC}")
        print(f"Multiplications a re-faire: {bcolors.FAIL}{len(failed)}{bcolors.ENDC}")
        print(f"{i} x {j} =")
        res = input()
        displayOnce = 0
        try:
            res = int(res.strip())
        except ValueError as e:
            print("ce n'est pas un nombre...")
            continue

        expected = i * j
        success = res == expected
        print(f"{i} x {j} = {expected}")
        if success:
            print(f"{bcolors.HEADER}bravo{bcolors.ENDC}\n")
            end_t = datetime.now()
            temps.append(end_t - start_t)
            return "success"
        print(f"{bcolors.FAIL}dommage{bcolors.ENDC}\n")
        return "failure"

        # except KeyboardInterrupt:
        #     print("finished")
        #     return


while to_do or failed:
    if to_do:
        ele = to_do.pop()
    elif failed:
        ele = failed.pop()
    res = exo(*ele)
    if res == "success":
        cpt_good += 1
        dones.append(ele)
    else:
        difficults.add(ele)
        cpt_bad += 1
        # errors are added twice
        failed.append(ele)
        i, j = ele
        failed.append((j, i))
        shuffle(failed)

print(f"{bcolors.HEADER}BRAVO c'est terminé {bcolors.ENDC}")
print(f"Tu as fait {bcolors.HEADER}{len(dones)}{bcolors.ENDC} multiplications")
print(f"Fautes: {bcolors.FAIL}{cpt_bad}{bcolors.ENDC}")
print(f"Difficiles: {bcolors.FAIL}{difficults}{bcolors.ENDC}")
seconds = [t.total_seconds() for t in temps]
somme = int(sum(seconds))
average = int(sum(seconds) / len(seconds))
print(f"Tu as mis {somme}s soit {average}s par réponse")
