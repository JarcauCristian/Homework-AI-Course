import random
import numpy as np


def init_chromosomes(number_of_chromosomes=6):
    chromosomes = []
    for i in range(number_of_chromosomes):
        r = random.randint(1, 63)
        chromosomes.append("{:06b}".format(r))
    return chromosomes


def make_f_and_p(chromosomes):
    f = []
    p = []
    for i in chromosomes:
        f.append(1/int(i, 2))

    for i in f:
        p.append(i/np.sum(f))
    return f, p


def rotate_genes(c1, c2, number_to_rotate):
    if 1 < number_to_rotate > 6:
        aux = c1[-1]
        c1 = c1[:-1] + c2[-1]
        c2 = c2[:-1] + aux
    else:
        aux = c1[-number_to_rotate:]
        c1 = c1[:-number_to_rotate] + c2[-number_to_rotate:]
        c2 = c2[:-number_to_rotate] + aux
    return c1, c2


def mutation(chromosomes):
    for i in range(len(chromosomes)):
        for j in range(len(chromosomes[i])):
            m = random.randint(1, 1000)
            if m == 299:
                if chromosomes[i][j] == '0':
                    chromosomes[i] = chromosomes[i][:j] + "1" + chromosomes[i][j+1:]
                elif chromosomes[i][j] == '1':
                    chromosomes[i] = chromosomes[i][:j] + "0" + chromosomes[i][j+1:]
    return chromosomes


c = init_chromosomes()
f, p = make_f_and_p(c)
print(f'{c}\n')
r = random.randint(1, 6)
i = 0
while i < len(c) - 1:
    c[i], c[i+1] = rotate_genes(c[i], c[i+1], r)
    i += 2

c = mutation(c)

print(f'{c}')
