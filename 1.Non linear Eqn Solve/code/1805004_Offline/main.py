import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import math

data_table = PrettyTable()
data_table.field_names = ["iterations", "xm", "error%", "f(xm)"]


def func(x):
    return ((x / (1 - x)) * ((6 / (2 + x)) ** .5)) - 0.05


def draw_graph():
    fig, ax = plt.subplots()
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    plt.grid(b=True, which='major', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', linestyle='-', alpha=0.3)
    plt.margins(x=0, y=0)

    x_val = np.linspace(-.5, .5, 2000)
    y_val = func(x_val)
    plt.plot(x_val, y_val, 'g')
    plt.title('f(x)')
    plt.show()


def method_bisection(low, high, approx_err, max_iter):
    new_mid = 0
    old_mid = 0
    for i in range(max_iter):
        new_mid = (low + high) / 2
        if i != 0:
            new_err = math.fabs((new_mid - old_mid) / new_mid) * 100
            if new_err < approx_err:
                return new_mid

        if func(low) * func(new_mid) < 0:
            high = new_mid
        elif func(low) * func(new_mid) > 0:
            low = new_mid
        else:
            return new_mid
        old_mid = new_mid

    return new_mid


def show_table(low, high, max_iter):
    old_mid = 0
    for i in range(max_iter):
        new_mid = (low + high) / 2
        if i != 0:
            new_err = math.fabs((new_mid - old_mid) / new_mid) * 100
            data_table.add_row([i + 1, new_mid, new_err, func(new_mid)])
        else:
            data_table.add_row([i + 1, new_mid, "-", func(new_mid)])

        if func(low) * func(new_mid) < 0:
            high = new_mid
        else:
            low = new_mid
        old_mid = new_mid

    print(data_table)


if __name__ == "__main__":
    draw_graph()
    print("root of the eqn: ", method_bisection(-.1, .2, .5, 20))
    show_table(-.1, .2, 20)
