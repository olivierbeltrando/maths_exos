import sys

from random import shuffle

from common import do_exercise, Operation

if __name__ == "__main__":
    tables = sys.argv[1:]
    print(f"revisions pour les tables de {tables}")
    to_do = []
    for i in tables:
        for j in range(11):
            to_do.append((int(i), j, Operation.Mult))

    # type "set" is not really ranmdom. shuffle ftw
    shuffle(to_do)
    do_exercise(to_do)
