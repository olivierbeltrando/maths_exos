from random import randint

from common import do_exercise, Operation


def gen_xx_number(number_zeros_max):
    return randint(1, 9) * pow(10, randint(0, number_zeros_max))


# 10 additions + x0 x00 x000
def gen_adds(number_additions, number_zeros_max):
    res = set()

    while len(res) < number_additions:
        # number a can be anything in the range
        a = randint(1, pow(10, number_zeros_max))
        # number b should be in the form x0, x00, x000, ...
        b = gen_xx_number(number_zeros_max)
        res.add((a, b, Operation.Add))
    return res


# 10 multiplications simples
def gen_multis(number_mults):
    res = set()
    while len(res) < number_mults:
        a = randint(1, 9)
        b = randint(1, 9)
        res.add((a, b, Operation.Mult))
    return res


# 10 +9 -9 +19 -19
def gen_nines(number, number_zeros_max):
    res = set()
    while len(res) < number:
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


# find compl for next full round of 10, 100, 1000, ...
def find_compl(number):
    nb_zeros = len(str(number))
    return pow(10, nb_zeros)


def test_find_compl():
    assert 10 == find_compl(3)
    assert 100 == find_compl(23)
    assert 1000 == find_compl(123)


def gen_compl_xx(quantity, number_zeros_max):
    res = set()
    while len(res) < quantity:
        a = randint(1, pow(10, number_zeros_max))
        b = find_compl(a)
        res.add((a, b, Operation.Compl))
    print(res)
    return res


if __name__ == "__main__":
    NUMBERS = 10
    NUMBER_ZERO_MAX = 3
    adds = gen_adds(NUMBERS, NUMBER_ZERO_MAX)
    mult = gen_multis(NUMBERS)
    nines = gen_nines(NUMBERS, NUMBER_ZERO_MAX)
    compls = gen_compl_xx(NUMBERS, NUMBER_ZERO_MAX)

    do_exercise(list(adds.union(mult).union(nines).union(compls)))
