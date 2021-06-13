import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import math

fig, ax = plt.subplots()

data_table = PrettyTable()
data_table.field_names = ["iterations", "estimation", "error%", "f(estimation)"]


def func(x):
    return ((x / (1 - x)) * ((6 / (2 + x)) ** .5)) - 0.05


def differentiation_func(x):
    return ((6 ** .5) * (x ** 2 + x + 4)) / (2 * ((x - 1) ** 2) * ((x + 2) ** 1.5))


def draw_graph():
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    plt.grid(b=True, which='major', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', linestyle='-', alpha=0.3)
    plt.margins(x=0, y=0)

    x_val = np.linspace(-.5, .5, 2000)
    y_val = func(x_val)
    plt.plot(x_val, y_val, 'g--')
    plt.title('f(x)')


def newton_raphson(est, approx_err, max_iter):
    new_est = 0
    for i in range(max_iter):
        new_est = est - func(est) / differentiation_func(est)
        new_err = math.fabs((new_est - est) / new_est) * 100
        if new_err < approx_err:
            plt.show()
            return new_est

        a = [est, new_est]
        b = [func(est), 0]
        plt.plot(a, b, 'b')

        est = new_est

    plt.show()
    return new_est


def show_table(est, max_iter):
    for i in range(max_iter):
        new_est = est - func(est) / differentiation_func(est)
        new_err = math.fabs((new_est - est) / new_est) * 100
        data_table.add_row([i + 1, new_est, new_err, func(new_est)])

        est = new_est

    print(data_table)


if __name__ == "__main__":
    draw_graph()
    print("root of the eqn: ", newton_raphson(.5, .5, 20))
    show_table(.5, 20)
