import csv
import random
import numpy as np


def sgn(data):
    if data < 0:
        return -1
    elif data > 0:
        return 1


def init_random_weights(p=2):
    w1 = []
    w2 = []
    w3 = []
    for i in range(p):
        w1.append(random.randint(0, 10))
        w2.append(random.randint(0, 10))
        w3.append(random.randint(0, 10))
    return np.array([w1, w2, w3])


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
        if i % 5 == 0 and learning_rate > 0:
            learning_rate -= 0.1
        for j in range(len(patterns)):
            min_from = list()
            min_from.append(np.dot(weights[0], patterns[j]))
            min_from.append(np.dot(weights[1], patterns[j]))
            min_from.append(np.dot(weights[2], patterns[j]))
            maxim = 1000000
            pos = 0
            for a, val in enumerate(weights):
                if maxim > np.dot(val, patterns[j]):
                    maxim = np.dot(val, patterns[j])
                    pos = a
            weights[pos] = weights[pos] + learning_rate*(patterns[j] - weights[pos])
            print(f'p1: {weights[0]}, p2: {weights[1]}, p3: {weights[2]} The prototype for pattern {j + 1}')
        print()


w = init_random_weights()
print(w)
x = read_patterns('patterns.csv')

winner_takes_all(x, w)
