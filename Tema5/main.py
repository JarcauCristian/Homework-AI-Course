import csv
import random
import numpy as np
import math


def sgn(data):
    if data < 0:
        return -1
    elif data > 0:
        return 1


def init_random_weights(dataset, p=3):
    weights = []
    mn1 = np.min(dataset[:, 0])
    mn2 = np.min(dataset[:, 1])
    mx1 = np.max(dataset[:, 0])
    mx2 = np.max(dataset[:, 0])
    for i in range(p):
        # r = random.randint(0, len(dataset) - 1)
        # while np.is in([dataset[r]], weights).all():
        #     r = random.randint(0, len(dataset) - 1)
        weights.append([random.randint(mn1, mx1), random.randint(mn2, mx2)])
    return np.array(weights)


def read_patterns(filepath: str):
    with open(filepath, 'r') as csv_in:
        csv_reader = csv.reader(csv_in)
        data = []
        for row in csv_reader:
            data.append(np.array([int(e) for e in row]))

    return np.array(data)


def winner_takes_all(patterns, weights, epochs=100, learning_rate=0.1):
    for i in range(epochs):
        print(f'Epoch: {i+1}')
        for j in range(len(patterns)):
            minim = 100000
            pos = 0
            for a, val in enumerate(weights):
                dt = math.sqrt((patterns[j][0] - val[0])**2 + (patterns[j][1] - val[1])**2)
                if minim > dt:
                    minim = dt
                    pos = a
            weights[pos] = weights[pos] + learning_rate*(patterns[j] - weights[pos])
            print(f'p1: {weights[0]}, p2: {weights[1]}, p3: {weights[2]} The prototype for pattern {j + 1}')
        print()
    return weights


x = read_patterns('patterns.csv')
w = init_random_weights(x, 4)
print(w)

wt = winner_takes_all(x, w)

p1 = []
p2 = []
p3 = []
p4 = []
for index in range(len(x)):
    mini = 100000
    ps = 0
    for ind, value in enumerate(wt):
        d = math.sqrt((x[index][0] - value[0])**2 + (x[index][1] - value[1])**2)
        if mini > d:
            mini = d
            ps = ind

    if ps == 0:
        p1.append(x[index])
    elif ps == 1:
        p2.append(x[index])
    elif ps == 2:
        p3.append(x[index])
    elif ps == 3:
        p4.append(x[index])

print(f'Patterns the are close to prototype 1: {np.array(p1)}\n Patterns the are close to prototype 2: {np.array(p2)}\n Patterns the are close to prototype 3: {np.array(p3)}\n Patterns the are close to prototype 4: {np.array(p4)}')
