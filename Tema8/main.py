import random
from collections import OrderedDict
import numpy as np
from decimal import *


def init_chromosomes(number_of_chromosomes=50):
    chromosomes = []
    for i in range(number_of_chromosomes):
        chromosomes.append("{:010b}".format(random.randint(0, 1024)))
    return chromosomes


def calculate_object_function(chromosome):
    getcontext().prec = 2
    s = 0
    p = 1
    for i in range(len(chromosome)):
        if chromosome[i] == '0':
            s += i+1
        elif chromosome[i] == '1':
            p *= (i+1)
    return float(Decimal(abs(36 - s) / 36) + Decimal(abs(360 - p) / 360))


def make_f_and_p(chromosomes):
    f = []
    p = {}
    for i in range(len(chromosomes)):
        f.append(calculate_object_function(chromosomes[i]))

    for i in range(len(f)):
        p[f[i] / np.sum(f)] = chromosomes[i]

    return f, p


def rotate_genes(c1, c2, number_to_rotate):
    if 1 < number_to_rotate > 10:
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


def get_min_max_from_ordered_dict(ordered_dict):
    minim = 10000000
    maxim = 0
    for i in ordered_dict.keys():
        if minim > i:
            minim = i
        if maxim < i:
            maxim = i
    return minim, maxim


def main():
    c = init_chromosomes()
    f, p = make_f_and_p(c)
    print(np.sum(f))
    p = OrderedDict(sorted(p.items()))
    while np.sum(f) < 10000:
        minim, maxim = get_min_max_from_ordered_dict(p)
        new_c = []
        for i in range(len(c)):
            r = random.uniform(np.min(minim), np.max(maxim))
            for key, value in p.items():
                if r < key:
                    new_c.append(c[c.index(value)])
                    break

        c = new_c

        i = 0
        r = random.randint(1, 10)
        while i < len(c) - 1:
            c[i], c[i + 1] = rotate_genes(c[i], c[i + 1], r)
            i += 2

        c = mutation(c)
        f, p = make_f_and_p(c)
        p = OrderedDict(sorted(p.items()))
    print(np.sum(f))


if __name__ == '__main__':
    main()
