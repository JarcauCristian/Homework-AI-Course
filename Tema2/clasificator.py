import numpy as np


def create_list():
    data = list()
    data.append(np.array([-1, -1, -1]))
    data.append(np.array([-1, -1, 1]))
    data.append(np.array([-1, 1, -1]))
    data.append(np.array([-1, 1, 1]))
    data.append(np.array([1, -1, -1]))
    data.append(np.array([1, -1, 1]))
    data.append(np.array([1, 1, -1]))
    data.append(np.array([1, 1, 1]))
    return np.array(data)


def weight_list(data: np.array, weight):
    return data * weight


def sgn_data(data):
    if data > 0:
        return 'class 1'
    elif data < 0:
        return 'class 2'


def memory_network(data):
    next_data = list()
    # first exit
    if data[1] * 1 + data[2] * (-1) > 0:
        next_data.append(1)
    elif data[1] * 1 + data[2] * (-1) == 0:
        next_data.append(data[0])
    elif data[1] * 1 + data[2] * (-1) < 0:
        next_data.append(-1)
    # second exit
    if data[0] * 1 + data[2] * (-1) > 0:
        next_data.append(1)
    elif data[0] * 1 + data[2] * (-1) == 0:
        next_data.append(data[1])
    elif data[0] * 1 + data[2] * (-1) < 0:
        next_data.append(-1)
    # third exit
    if data[0] * (-1) + data[1] * (-1) > 0:
        next_data.append(1)
    elif data[0] * (-1) + data[1] * (-1) == 0:
        next_data.append(data[2])
    elif data[0] * (-1) + data[1] * (-1) < 0:
        next_data.append(-1)
    if data == next_data:
        return data
    else:
        return memory_network(next_data)


points = create_list()
points = weight_list(points, [1, 1, 1])

for point in points:
    print(f'Point {point} is from {sgn_data(np.sum(point))}')

print('\n')

for index, point in enumerate(create_list()):
    if list(point) == memory_network(list(point)):
        print(f'Point {index} is a stable point')
