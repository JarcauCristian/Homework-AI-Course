def f(x):
    return 6*(x**2) - 12*x + 1


def df(x):
    return 12*x - 12


def g(x, y):
    return x**2 + 2*y**2


def dgx(x):
    return 2*x


def dgy(y):
    return 4*y


def h(x, y):
    return (1-x)**2 + 100*(x - y**2)**2


def dhx(x, y):
    return - 2 + 202*x - 200*y**2


def dhy(x, y):
    return -400*y*(x - y**2)
