import csv
import random


def read_data():
    with open('Salary_Data.csv', 'r') as csv_in:
        csv_reader = csv.reader(csv_in)
        year_of_exp, salary = [], []
        for i, row in enumerate(csv_reader):
            if i == 0:
                continue
            else:
                year_of_exp.append(float(row[0]))
                salary.append(float(row[1]))
        return year_of_exp, salary


def function(i, j, w1, w2):
    n = len(i)
    s = 0
    for k in range(len(i)):
        s += (j[k] - (w1 * i[k] + w2))**2
    return -(1 / (2*n)) * s


def dw1(i, j, w1, w2):
    n = len(i)
    s = 0
    for k in range(len(i)):
        s += (j[k] - (w1*i[k] + w2))*i[k]
    return -(1/n)*s


def dw2(i, j, w1, w2):
    n = len(i)
    s = 0
    for k in range(len(i)):
        s += j[k] - (w1*i[k] + w2)
    return -(1/n)*s


def gradient_descent(x, y, w1, w2, iteration, learning_rate=0.01, threshold=0.000001):
    data_w1 = list()
    data_w2 = list()
    data_w1.append(w1)
    data_w2.append(w2)
    for i in range(iteration):
        print(f'Iteration {i+1}')
        new_data_w1 = data_w1[i] - learning_rate * dw1(x, y, data_w1[i], data_w2[i])
        new_data_w2 = data_w2[i] - learning_rate * dw2(x, y, data_w1[i], data_w2[i])
        data_w1.append(new_data_w1)
        data_w2.append(new_data_w2)
        if abs(data_w1[-1] - data_w1[-2]) <= threshold and abs(data_w2[-1] - data_w2[-2]) <= threshold:
            break
    print(f'w1 = {data_w1[-1]}; w2 = {data_w2[-1]}')


x_data, y_data = read_data()
start_w1 = random.randint(0, 10)
start_w2 = random.randint(0, 10)
print(start_w1, start_w2)
gradient_descent(x_data, y_data, start_w1, start_w2, 10000)
