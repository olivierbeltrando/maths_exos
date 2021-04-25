from random import randint

from common import do_exercise, Operation


# 10 additions + x0 x00 x000
def gen_adds(number_additions, number_zeros_max):
    res = set()

    def gen_xx_number():
        return randint(1, 9) * pow(10, randint(0, number_zeros_max))

    while len(res) != number_additions:
        # number a can be anything in the range
        a = randint(1, pow(10, number_zeros_max))
        # number b should be in the form x0, x00, x000, ...
        b = gen_xx_number()
        res.add((a, b, Operation.Add))
    return res


# 10 multiplications simples
def gen_multis(number_mults):
    res = set()
    while len(res) != number_mults:
        a = randint(1, 9)
        b = randint(1, 9)
        res.add((a, b, Operation.Mult))
    return res


# 10 +9 -9 +19 -19
def gen_nines(number, number_zeros_max):
    res = set()
    while len(res) != number:
        # number a can be anything in the range
        a = randint(1, pow(10, number_zeros_max))
        # b is either 9, 19
        b = 9 + randint(0, 1) * 10
        # b is either -9 or -19
        operation = Operation.Add
        if randint(1, 2) % 2 == 0:
            operation = Operation.Sub
        res.add((a, b, operation))
    return res


if __name__ == "__main__":
    NUMBERS = 10
    NUMBER_ZERO_MAX = 3
    adds = gen_adds(NUMBERS, NUMBER_ZERO_MAX)
    mult = gen_multis(NUMBERS)
    nines = gen_nines(NUMBERS, NUMBER_ZERO_MAX)

    do_exercise(list(adds.union(mult).union(nines)))
