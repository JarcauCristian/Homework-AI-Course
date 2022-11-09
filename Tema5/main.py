import csv
import random
import numpy as np


def sgn(data):
    if data < 0:
        return -1
    elif data > 0:
        return 1


def init_random_weights(dataset, p=3):
    weights = []
    for i in range(p):
        weights.append(dataset[random.randint(0, len(dataset) - 1)])
    return np.array(weights)


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
            maxim = 100000
            pos = 0
            for a, val in enumerate(weights):
                if maxim > np.linalg.norm(patterns[j] - val):
                    maxim = np.linalg.norm(patterns[j] - val)
                    pos = a
            weights[pos] = weights[pos] + learning_rate*(patterns[j] - weights[pos])
            print(f'p1: {weights[0]}, p2: {weights[1]}, p3: {weights[2]} The prototype for pattern {j + 1}')
        print()


x = read_patterns('patterns.csv')
w = init_random_weights(x)
print(w)

winner_takes_all(x, w)
