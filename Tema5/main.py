import csv
import random
import numpy as np


def init_random_weights(p=3):
    w1 = []
    w2 = []
    for i in range(p):
        w1.append(random.randint(10, 200))
        w2.append(random.randint(10, 200))
    return np.array([w1, w2])


def read_patterns(filepath: str):
    with open(filepath, 'r') as csv_in:
        csv_reader = csv.reader(csv_in)
        data = []
        for row in csv_reader:
            data.append(np.array([int(e) for e in row]))

    return np.array(data)


def winner_takes_all(patterns, weights, epochs=20, learning_rate=1):
    for i in range(epochs):
        print(f'Epoch: {i+1}')
        for j in range(len(patterns)):
            min_from = list()
            min_from.append(patterns[j] - weights[:, 0])
            min_from.append(patterns[j] - weights[:, 1])
            min_from.append(patterns[j] - weights[:, 2])
            min_from = np.array(min_from)
            dct = {}
            minim = []
            for k, val in enumerate(min_from):
                dct[k] = np.sum(val)
                minim.append(np.sum(val))
            minim = np.min(minim)
            index = [key for key, value in dct.items() if value == minim][0]
            weights[:, index] = weights[:, index] + learning_rate*min_from[index]
            print(f'{weights} The prototype for pattern {j + 1}')


w = init_random_weights()
x = read_patterns('patterns.csv')

winner_takes_all(x, w)
