import random
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
    return float(Decimal((abs(s - 36)) / 36) + Decimal((abs(p - 360)) / 360))


def make_f(chromosomes):
    f = {}
    for i in range(len(chromosomes)):
        f[i] = calculate_object_function(chromosomes[i])

    return f


def make_sorted_dict(dct):
    return {k: v for k, v in sorted(dct.items(), key=lambda item: item[1])}


def select_new_chromosomes(chromosomes, f, number_to_rotate=2):
    lst = [e for e in f.keys()]
    lst = [chromosomes[e] for e in lst]
    lst[-2] = lst[0]
    lst[-1] = lst[1]
    return lst

# Sortez populatia dupa valoarea functiei obiectiv, dupa care pe ultimi doi ii elimini si ii inlocuiesc cu primi doi
# Crossover doar 2 cromozomi
# Mutation 5 mutations
# 10000 de iteratii sau cromozom cu functie obiectiv 0


def rotate_genes(chromosomes, crossover=2, number_to_rotate=5):
    for i in range(crossover):
        c1 = random.randint(0, 49)
        c2 = random.randint(0, 49)
        aux = chromosomes[c1][-number_to_rotate:]
        chromosomes[c1] = chromosomes[c1][:-number_to_rotate] + chromosomes[c2][-number_to_rotate:]
        chromosomes[c2] = chromosomes[c2][:-number_to_rotate] + aux
    return chromosomes


def mutation(chromosomes, mutation_number=5):
    for i in range(mutation_number):
        r = random.randint(0, 49)
        g = random.randint(0, 9)
        if g == 9:
            if chromosomes[r][g] == '0':
                chromosomes[r] = chromosomes[r][:g] + "1"
            elif chromosomes[r][g] == '1':
                chromosomes[r] = chromosomes[r][:g] + "0"
        else:
            if chromosomes[r][g] == '0':
                chromosomes[r] = chromosomes[r][:g] + "1" + chromosomes[r][g+1:]
            elif chromosomes[r][g] == '1':
                chromosomes[r] = chromosomes[r][:g] + "0" + chromosomes[r][g + 1:]
    return chromosomes


def main():
    c = init_chromosomes()
    ok = 0
    for i in range(10000):
        print(f'Iteration {i}')
        f = make_f(c)
        for key, value in f.items():
            if value == 0:
                print(f'Chromosome {c[key]} fulfil the condition')
                ok = 1
        if ok == 1:
            break
        f = make_sorted_dict(f)
        c = select_new_chromosomes(c, f)
        c = rotate_genes(c)
        c = mutation(c)


if __name__ == '__main__':
    main()
