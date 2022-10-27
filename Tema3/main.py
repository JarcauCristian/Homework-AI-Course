import random
import functions as f


def gradient_descent(start_x, iteration, learning_rate):
    data = list()
    data.append(start_x)
    for i in range(iteration):
        data.append(data[i] - learning_rate * f.df(data[i]))
        print(f'At iteration {i+1} the function is {f.f(data[i] - learning_rate * f.df(data[i]))}')
        if abs(data[-1] - data[-2]) <= 0.00001:
            break


def gradient_descent_g_func(start_x, start_y, iteration, learning_rate):
    data_x = list()
    data_y = list()
    data_x.append(start_x)
    data_y.append(start_y)
    for i in range(iteration):
        new_x = data_x[i] - learning_rate * f.dgx(data_x[i])
        new_y = data_y[i] - learning_rate * f.dgy(data_y[i])
        data_x.append(new_x)
        data_y.append(new_y)
        print(f'At iteration {i+1} the function is {f.g(new_x, new_y)}')
        if f.g(new_x, new_y) > 1e+10:
            print("Function goes to infinity! Minim undefined!")
            break
        if abs(data_x[-1] - data_x[-2]) <= 0.00001 and abs(data_y[-1] - data_y[-2]) <= 0.00001:
            break


def gradient_descent_h_func(start_x, start_y, iteration, learning_rate):
    data_x = list()
    data_y = list()
    data_x.append(start_x)
    data_y.append(start_y)
    for i in range(iteration):
        new_x = data_x[i] - learning_rate * f.dhx(data_x[i], data_y[i])
        new_y = data_y[i] - learning_rate * f.dhy(data_x[i], data_y[i])
        data_x.append(new_x)
        data_y.append(new_y)
        print(f'At iteration {i+1} the function is {f.h(new_x, new_y)}')
        if f.h(new_x, new_y) > 1e+10:
            print("Function goes to infinity! Minim undefined!")
            break
        if abs(data_x[-1] - data_x[-2]) <= 0.00001 and abs(data_y[-1] - data_y[-2]) <= 0.00001:
            break


print('\nFunction f(x) = 6*x^2 - 12*x + 1')
start = random.randint(0, 10)
print(f'x0: {start}')
gradient_descent(start, 20, 0.1)

print('\nFunction g(x, y) = x^2 - 2*y^2')
x_start = random.randint(0, 10)
y_start = random.randint(0, 10)
print(f'x0: {x_start}; y0: {y_start}')
gradient_descent_g_func(x_start, y_start, 100, 0.1)

print('\nFunction h(x, y) = (1-x)^2 + 100*(x - y^2)^2')
x_start = random.randint(0, 10)
y_start = random.randint(0, 10)
print(f'x0: {x_start}; y0: {y_start}')
gradient_descent_h_func(x_start, y_start, 100, 0.1)
