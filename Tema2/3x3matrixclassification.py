import csv
import numpy as np


def sgn_pos(sum_pond):
    if sum_pond < 0:
        return 0
    else:
        return 1


def read_data(path):
    with open(path, 'r') as csv_in:
        csv_reader = csv.reader(csv_in)
        all_data = []
        data = list()
        for i, row in enumerate(csv_reader):
            if i % 3 == 0 and i > 0:
                all_data.append(np.array(data, dtype=float))
                data.clear()
            data.append(row)
        all_data.append(np.array(data, dtype=float))
    return all_data


unaltered_data = read_data("data_matrix.csv")
altered_data = read_data("altered_data.csv")
weights = np.array([[-0.65, -0.41, 0.15], [0.19, 0.59, 0.04], [-0.95, 0.77, 0.55]])
print("Results for unaltered data:")
for index, matrix in enumerate(unaltered_data):
    print(f'For matrix {index} the neuron response is: {sgn_pos(np.sum(weights * matrix))}')

print("\nResults for altered data:")
for index, matrix in enumerate(altered_data):
    print(f'For matrix {index} the neuron response is: {sgn_pos(np.sum(weights * matrix))}')
