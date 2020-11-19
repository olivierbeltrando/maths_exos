import os
import sys

from datetime import datetime

to_do = set()
dones = set()
failed = set()

tables = sys.argv[1:]
print(f"revisions pour les tables de {tables}")
for i in tables:
    for j in range(11):
        to_do.add((int(i), j))


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
    print(f"{i} x {j} =")
    start_t = datetime.now()
    while True:
        res = input()
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
    os.system("clear")
    print(f"Multiplications a faire: {bcolors.HEADER}{len(to_do)}{bcolors.ENDC}")
    print(f"Multiplications a re-faire: {bcolors.FAIL}{len(failed)}{bcolors.ENDC}")
    res = exo(*ele)
    if res == "success":
        dones.add(ele)
    else:
        # errors are added twice
        failed.add(ele)
        i, j = ele
        failed.add((j, i))

print(f"{bcolors.HEADER}BRAVO c'est terminé {bcolors.ENDC}")
print(f"Tu as fait {bcolors.HEADER}{len(dones)}{bcolors.ENDC} multiplications")
seconds = [t.total_seconds() for t in temps]
somme = int(sum(seconds))
average = int(sum(seconds) / len(seconds))
print(f"Tu as mis {somme}s soit {average}s par réponse")
