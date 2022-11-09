import csv
import numpy as np
import random


def clusters_initialize(dataset, nr_clusters: int):
    clusters = []
    m = len(dataset) - 1
    for i in range(nr_clusters):
        clusters.append(dataset[random.randint(0, m-1)])
    return np.array(clusters)


def read_patterns(filepath: str):
    with open(filepath, 'r') as csv_in:
        csv_reader = csv.reader(csv_in)
        data = []
        for row in csv_reader:
            data.append(np.array([int(e) for e in row]))

    return np.array(data)


def k_mean_clustering(patterns, clusters):
    old_cluster = np.array([[0, 0], [0, 0], [0, 0]])
    cp = {}
    while not np.array_equal(old_cluster, clusters):
        groups = {}
        old_cluster = np.array(clusters)
        for i in range(len(patterns)):
            minim = 100000
            pos = 0
            for j, value in enumerate(clusters):
                mean_dist = abs(value[0] - patterns[i][0]) + abs(value[1] - patterns[i][1])
                if minim > mean_dist:
                    minim = mean_dist
                    pos = j
            groups[i] = pos
        c1_x = 0
        c1_y = 0
        c1_t = 0
        c2_x = 0
        c2_y = 0
        c2_t = 0
        c3_x = 0
        c3_y = 0
        c3_t = 0
        for key, value in groups.items():
            if value == 0:
                c1_x += patterns[key][0]
                c1_y += patterns[key][1]
                c1_t += 1
            elif value == 1:
                c2_x += patterns[key][0]
                c2_y += patterns[key][1]
                c2_t += 1
            elif value == 2:
                c3_x += patterns[key][0]
                c3_y += patterns[key][1]
                c3_t += 1
        if c1_t != 0:
            clusters[0][0] = c1_x/c1_t
            clusters[0][1] = c1_y/c1_t
        if c2_t != 0:
            clusters[1][0] = c2_x/c2_t
            clusters[1][1] = c2_y/c2_t
        if c3_t != 0:
            clusters[2][0] = c3_x/c3_t
            clusters[2][1] = c3_y/c3_t
        cp = groups
    print(f'Final centroids: \n{clusters}')
    for key, value in cp.items():
        print(f'Point P{key} in cluster {value}')


x = read_patterns('patterns.csv')
k = clusters_initialize(x, 3)
print(f'Initial centroids: \n{k}\n')
k_mean_clustering(x, k)
