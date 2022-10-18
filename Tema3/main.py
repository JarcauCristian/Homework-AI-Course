import numpy as np


def f(x):
    return 6*x**2 - 12*x - 1


def df(x):
    return 12*x - 12


def gradient_descent(start_x, iteration, learning_rate):
    data = list()
    data.append(start_x)
    for i in range(iteration):
        data.append(data[i] - learning_rate * df(data[i]))
        print(data[i] - learning_rate * df(data[i]))
        if -0.01 < data[i] - learning_rate * df(data[i]) < 0.001:
            break


gradient_descent(-1, 100, 0.01)
