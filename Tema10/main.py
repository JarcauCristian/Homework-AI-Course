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
            result = []
            for i in row:
                result.append(int(i))
            results.append(result)

    return np.array(results)


def initialize_weights(number_of_perceptrons):
    weights = []
    for i in range(number_of_perceptrons):
        weight = []
        for j in range(number_of_perceptrons):
            weight.append(random.uniform(-1, 1))
        weights.append(weight)
    return np.array(weights)


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


def delta_rule(patterns, results, weights, learning_rate=0.1, epochs=10000, max_error=0.01):
    for i in range(epochs):
        print(f'Epoch {i+1}')
        e = 0
        # Calculate Global error
        for j in range(len(patterns)):
            o = []
            # Calculate exits
            for k in range(len(weights)):
                net = np.dot(weights[k], patterns[j])
                o.append(activation_function(net))

            # Update weights
            for k in range(len(weights)):
                for v in range(len(weights[k])):
                    weights[k][v] = weights[k][v] + (learning_rate * (results[j][k] - o[k]) * (1 - o[k]**2) * patterns[j][v])

            # Calculate local error
            for k in range(len(o)):
                e += (results[j][k] - o[k]) ** 2
        if e < max_error:
            print(e)
            break
        print(e)
    return weights


def exits(patterns, weights):
    for i in range(len(patterns)):
        o = []
        for j in weights:
            net = np.dot(j, patterns[i])
            o.append(activation_function(net))
        print(f'Exits for pattern {i+1}: {o}')


y = read_patterns()
d = read_results()
w = initialize_weights(3)
y = normalize_patterns(y)
print(y)
new_w = delta_rule(y, d, w)
exits(y, new_w)
