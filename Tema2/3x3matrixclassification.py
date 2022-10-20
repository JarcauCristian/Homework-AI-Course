import csv
import numpy as np


def sgn_pos(sum_pond):
    return 1 if sum_pond > 0 else 0


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
weights = np.array([[-0.14, 0.06, -0.28], [-0.93, -0.08, 0.28], [-0.64, 0.47, -0.85]])
print("Results for unaltered data:")
for index, matrix in enumerate(unaltered_data):
    print(f'For matrix {index} the neuron response is: {sgn_pos(np.sum(weights * matrix))}')

print("\nResults for altered data:")
for index, matrix in enumerate(altered_data):
    print(f'For matrix {index} the neuron response is: {sgn_pos(np.sum(weights * matrix))}')

counter = 0
for index in range(4):
    if sgn_pos(np.sum(weights * altered_data[index])) == sgn_pos(np.sum(weights * unaltered_data[index])):
        counter += 1

print(f'The rate of correct classification is: {counter/len(altered_data) * 100}%')
