import sys

from random import shuffle

from common import do_exercise, Operation


def gen_tables(numbers):
    to_do = []
    for i in numbers:
        for j in range(11):
            to_do.append((int(i), j, Operation.Mult))
    # type "set" is not really ranmdom. shuffle ftw
    shuffle(to_do)
    return to_do


if __name__ == "__main__":
    numbers = sys.argv[1:]
    print(f"revisions pour les tables de {numbers}")
    to_do = gen_tables(numbers)
    do_exercise(to_do)
