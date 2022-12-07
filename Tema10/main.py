import csv
import math
import random
import numpy as np


def activation_function(net):
    return (2/(1 + math.e**(-net))) - 1


def read_patterns():
    with open('patterns.csv', 'r') as csv_in:
        csv_reader = csv.reader(csv_in)
        patterns = []
        for row in csv_reader:
            pattern = []
            for i in row:
                pattern.append(int(i))
            patterns.append(pattern)

    return np.array(patterns)


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


def delta_rule(patterns, results, weights, learning_rate=1, max_error=0.01):
    e = 10
    while e >= max_error:
        e = 0
        for i in range(len(patterns)):
            o = []
            for j in range(len(weights)):
                net = np.dot(weights[j], patterns[i])
                o.append(activation_function(net))
            for j in range(len(weights)):
                weights[j] += learning_rate * (1/2) * (results[i] - o) * (1 - np.array([e**2 for e in o])) * patterns[i]
            i_e = 0
            for j in range(len(results[i])):
                i_e += (results[i][j] - o[j])**2
            e = e + i_e
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
new_w = delta_rule(y, d, w)
exits(y, new_w)
