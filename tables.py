import sys

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


def exo(i, j):
    print(f"{i} x {j} =")
    while True:
        try:
            res = input()
        except ValueError as e:
            print("ce n'est pas un nombre...")

        res = int(res.strip())
        expected = i * j
        success = res == expected
        print(f"{i} x {j} = {expected}")
        if success:
            print(f"{bcolors.HEADER}bravo{bcolors.ENDC}\n")
            return "success"
        print(f"{bcolors.FAIL}dommage{bcolors.ENDC}\n")
        return "failure"

        # except KeyboardInterrupt:
        #     print("finished")
        #     return


while to_do:
    for ele in to_do:
        res = exo(*ele)
        if res == "success":
            dones.add(ele)
        else:
            # errors are added twice
            failed.add(ele)
            i, j = ele
            failed.add((j, i))
    to_do = failed
    failed = set()

print(f"{bcolors.HEADER}BRAVO c'est terminé {bcolors.ENDC}")
print(f"Tu as fait {bcolors.HEADER}{len(dones)}{bcolors.ENDC} multiplications")
