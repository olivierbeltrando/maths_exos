from random import randint

from common import do_exercise, Op


# 10 additions + x0 x00 x000
def gen_adds(nb_additions, nb_zeros_max):
    res = set()

    def gen_xx_nb():
        return randint(1, 9) * pow(10, randint(0, nb_zeros_max))

    while len(res) != nb_additions:
        # number a can be anything in the range
        a = randint(1, pow(10, nb_zeros_max))
        # number b should be in the form x0, x00, x000, ...
        b = gen_xx_nb()
        res.add((a, b, Op.Add))
    return res


# 10 multiplications simples
def gen_multis(nb_mults):
    res = set()
    while len(res) != nb_mults:
        a = randint(1, 9)
        b = randint(1, 9)
        res.add((a, b, Op.Mult))
    return res


# 10 +9 -9 +19 -19
def gen_nines(nb, nb_zeros_max):
    res = set()
    while len(res) != nb:
        # number a can be anything in the range
        a = randint(1, pow(10, nb_zeros_max))
        # b is either 9, 19
        b = 9 + randint(0, 1) * 10
        # b is either -9 or -19
        operation = Op.Add
        if randint(1, 2) % 2 == 0:
            operation = Op.Sub
        res.add((a, b, operation))
    return res


if __name__ == "__main__":
    nb = 10
    nb_zero_max = 3
    adds = gen_adds(nb, nb_zero_max)
    mult = gen_multis(nb)
    nines = gen_nines(nb, nb_zero_max)

    do_exercise(list(adds.union(mult).union(nines)))
