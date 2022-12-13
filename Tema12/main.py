import csv
import math
import random
import numpy as np


def activation_function(net):
    return (2/(1 + math.pow(math.e, -net))) - 1


def read_patterns():
    with open('patterns.csv', 'r') as csv_in:
        csv_reader = csv.reader(csv_in)
        patterns = []
        for row in csv_reader:
            pattern = []
            for i in row:
                pattern.append(int(i))
            patterns.append(pattern)

    return np.array(patterns, dtype=float)


def read_results():
    with open('results.csv', 'r') as csv_in:
        csv_reader = csv.reader(csv_in)
        results = []
        for row in csv_reader:
            results.append(int(row[0]))

    return np.array(results)


def normalize_patterns(patterns):
    min_col = list()
    max_col = list()
    min_col.append(np.min(patterns[:, 0]))
    min_col.append(np.min(patterns[:, 1]))
    max_col.append(np.max(patterns[:, 0]))
    max_col.append(np.max(patterns[:, 1]))
    for i in range(2):
        patterns[:, i] = 2 * (patterns[:, i] - min_col[i]) / (max_col[i] - min_col[i]) - 1

    return patterns


def initialize_weights(number_of_perceptrons):
    weights = []
    for i in range(number_of_perceptrons):
        weight = []
        for j in range(3):
            weight.append(random.uniform(-1, 1))
        weights.append(weight)
    return np.array(weights)


def initialize_outer_weights(number_of_perceptrons):
    weights = []
    for i in range(number_of_perceptrons):
        weight = []
        for j in range(4):
            weight.append(random.uniform(-1, 1))
        weights.append(weight)
    return np.array(weights)


def backpropagation(patterns, results, inner_weights, outer_weights, learning_rate=1.9, epochs=1000000, max_error=0.01):
    for i in range(epochs):
        print(f'Epoch {i+1}')
        e = 0
        for j in range(len(patterns)):
            hidden_layer = []
            for k in range(len(inner_weights)):
                net = np.dot(inner_weights[k], patterns[j])
                hidden_layer.append(activation_function(net))

            hidden_layer.append(-1)

            net = np.dot(outer_weights, hidden_layer)
            outer_layer = activation_function(net)

            delta_ok = 0.5 * (results[j] - outer_layer) * (1 - outer_layer**2)
            delta_yj = list()

            for k in range(len(outer_weights[0])):
                delta_yj.append(0.5 * (1 - hidden_layer[k] ** 2) * delta_ok * outer_weights[0][k])

            for k in range(len(inner_weights)):
                for s in range(len(inner_weights[k])):
                    inner_weights[k][s] = inner_weights[k][s] + learning_rate * delta_yj[k] * patterns[j][s]

            for k in range(len(outer_weights)):
                for s in range(len(outer_weights[k])):
                    outer_weights[k][s] = outer_weights[k][s] + learning_rate * delta_ok * hidden_layer[k]

            e += 0.5 * (results[j] - outer_layer)**2

        if e < max_error:
            print(e)
            break
        print(e)

    return inner_weights, outer_weights


def exits(patterns, inner_weights, outer_weights):
    for i in range(len(patterns)):
        hidden_layer = []
        for k in range(len(inner_weights)):
            net = np.dot(inner_weights[k], patterns[i])
            hidden_layer.append(activation_function(net))

        hidden_layer.append(-1)

        net = np.dot(outer_weights, hidden_layer)
        outer_layer = activation_function(net)
        print(f'Exit for pattern {i + 1}: {outer_layer}')


y = read_patterns()
d = read_results()
v = initialize_weights(3)
w = initialize_outer_weights(1)
y = normalize_patterns(y)
new_v, new_w = backpropagation(y, d, v, w)
exits(y, new_v, new_w)
