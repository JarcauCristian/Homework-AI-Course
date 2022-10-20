import math
import numpy as np


def sgn(data):
    return -1 if data < 0 else 1


def bipolar_continuum_function(net, lmb=1):
    return (2/1+math.e**(-lmb*net))-1


def bipolar_hebbian(weight, data, dt_len=1):
    weights = list()
    weights.append(weight)
    for i in range(dt_len):
        dt_sgn = sgn(np.dot(weights[i], data[i]))
        weights.append(weights[i] + dt_sgn*data[i])
    return np.array(weights)


def bipolar_continuum_hebbian(weight, data, dt_len=1):
    weights = list()
    weights.append(weight)
    for i in range(dt_len):
        dt_sgn = bipolar_continuum_function(np.dot(weights[i], data[i]))
        weights.append(weights[i] + dt_sgn*data[i])
    return np.array(weights)


x = np.array([[1, -2, 1.5, 0], [1, -0.5, -2, -1.5], [0, 1, -1, 1.5]])
initial_weight = np.array([1, -1, 0, 0.5])
bipolar = bipolar_hebbian(initial_weight, x, 3)
print('\nBipolar binary function hebbian')
for index in range(len(bipolar)):
    print(f'Weight {index+1}: {bipolar[index]}')

continuum = bipolar_continuum_hebbian(initial_weight, x, 3)
print('\nBipolar continuum function hebbian')
for index in range(len(continuum)):
    print(f'Weight {index+1}: {continuum[index]}')

x2 = np.array([[1, -2], [0, 1], [2, 3], [1, -1]])
w1 = np.array([1, -1])

bipolar = bipolar_hebbian(w1, x2, 4)
print('\nBipolar binary function hebbian for second array')
for index in range(len(bipolar)):
    print(f'Weight {index+1}: {bipolar[index]}')

continuum = bipolar_continuum_hebbian(w1, x2, 4)
print('\nBipolar continuum function hebbian for second array')
for index in range(len(continuum)):
    print(f'Weight {index+1}: {continuum[index]}')
