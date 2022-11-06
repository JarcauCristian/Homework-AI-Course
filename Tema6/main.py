import numpy as np


def sgn(data):
    if data < 0:
        return -1
    elif data > 0:
        return 1


def perceptron_rule(patterns, weights, response, learning_rate=0.1):
    """
    :param patterns: The list of patterns
    :param weights: The list of initial weights
    :param response: The list of awaited responses
    :param learning_rate: The learning rate of the code
    :return:
    """
    last_weight = np.array([])
    counter = 1
    while not np.array_equal(last_weight, weights):
        last_weight = weights
        print(f'Epoch {counter}')
        for i in range(len(patterns)):
            net = np.dot(weights, patterns[i])
            print(f'{net} Net for x{i+1}')
            sgn_net = sgn(net)
            weights = weights + learning_rate*(response[i] - sgn_net)*patterns[i]
        print()
        counter += 1


w = np.array([0, 1, 0])
x = np.array([[2, 1, -1], [0, -1, -1]])
d = np.array([-1, 1])

perceptron_rule(x, w, d)
