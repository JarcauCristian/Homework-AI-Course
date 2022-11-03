import math
import numpy as np


def sgn(data):
    return -1 if data < 0 else 1


def bipolar_continuum_function(net, lmb=1):
    return (1-math.e**(-lmb*net))/(1+math.e**(-lmb*net))


def bipolar_hebbian(weight, data, dt_len=1, learning_rate=1, epochs=10):
    for j in range(epochs):
        weights = list()
        weights.append(weight)
        for i in range(dt_len):
            dt_sgn = sgn(np.dot(weights[i], data[i]))
            weights.append(weights[i] + learning_rate*dt_sgn*data[i])
        weight = weights[-1]
        print(f'Weights at epoch {j+1}')
        for k, value in enumerate(np.array(weights)):
            print(f'Weight {k+1}: {value}')
        print()


def bipolar_continuum_hebbian(weight, data, dt_len=1, learning_rate=1, epochs=10):
    for j in range(epochs):
        weights = list()
        weights.append(weight)
        for i in range(dt_len):
            dt_sgn = bipolar_continuum_function(np.dot(weights[i], data[i]))
            weights.append(weights[i] + learning_rate*dt_sgn*data[i])
        weight = weights[-1]
        print(f'Weights at epoch {j+1}')
        for k, value in enumerate(np.array(weights)):
            print(f'Weight {k+1}: {value}')
        print()


x = np.array([[1, -2, 1.5, 0], [1, -0.5, -2, -1.5], [0, 1, -1, 1.5]])
print(f'x: {x}')
initial_weight = np.array([1, -1, 0, 0.5])
print('\nBipolar binary function hebbian')
bipolar_hebbian(initial_weight, x, 3, 0.1)

print('\nBipolar continuum function hebbian')
bipolar_continuum_hebbian(initial_weight, x, 3, 0.1)

x2 = np.array([[1, -2], [0, 1], [2, 3], [1, -1]])
w1 = np.array([1, -1])
print(f'x2: {x2}')
print('\nBipolar binary function hebbian for second array')
bipolar_hebbian(w1, x2, 4, 0.1)

print('\nBipolar continuum function hebbian for second array')
bipolar_continuum_hebbian(w1, x2, 4, 0.1)
