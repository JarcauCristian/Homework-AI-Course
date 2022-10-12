import csv
import numpy as np

with open('iris.data', 'r') as csv_in:
    csv_reader = csv.reader(csv_in)
    data = []
    for row in csv_reader:
        if len(row) == 5:
            data.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])

np_list = np.array(data)
min_cols = list()
min_cols.append(min(np_list[:, 0]))
min_cols.append(min(np_list[:, 1]))
min_cols.append(min(np_list[:, 2]))
min_cols.append(min(np_list[:, 3]))
max_cols = list()
max_cols.append(max(np_list[:, 0]))
max_cols.append(max(np_list[:, 1]))
max_cols.append(max(np_list[:, 2]))
max_cols.append(max(np_list[:, 3]))
mean_cols = list()
mean_cols.append(np.mean(np_list[:, 0]))
mean_cols.append(np.mean(np_list[:, 1]))
mean_cols.append(np.mean(np_list[:, 2]))
mean_cols.append(np.mean(np_list[:, 3]))
median_cols = list()
median_cols.append(np.median(np_list[:, 0]))
median_cols.append(np.median(np_list[:, 1]))
median_cols.append(np.median(np_list[:, 2]))
median_cols.append(np.median(np_list[:, 3]))
for i in range(0, 4):
    print(f"Metadate col {i}: {min_cols[i]}, {max_cols[i]}, {mean_cols[i]}, {median_cols[i]}")

print(f"The initial list: \n{np_list}\n")
for i in range(0, 4):
    np_list[:, i] = (np_list[:, i] - min_cols[i]) / (max_cols[i] - min_cols[i])

print(f"The normalized list: \n{np_list}\n")

np_list_bk = np.sum(np_list * np.array([0.2, 1.1, -0.9, 1]), axis=1)
np_list = np.append(np_list, np_list_bk.reshape(150, 1), axis=1)
print(f"The weighted list: \n{np_list}")

with open('normalized_data.data', 'w', newline='') as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerows(np_list)
