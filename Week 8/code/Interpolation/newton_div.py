import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import math


class COLORS:
    RESET = '\033[0m'
    HEADER = '\033[96m'
    BLUE = '\033[94m'
    FAIL = '\033[91m'


data_table = PrettyTable()
data_table.field_names = ["order of polynomial", "f(x)", "error%"]


def draw_graph(array_X, array_Y):
    fig, ax = plt.subplots()
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    plt.grid(b=True, which='major', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', linestyle='-', alpha=0.3)
    plt.margins(x=0, y=0)
    n = len(array_X)

    x_values = np.linspace(array_X[0], array_X[n - 1], 50)
    y_values = np.zeros(50)
    for i in range(len(x_values)):
        y_values[i] = newton_div_difference(array_X, array_Y, x_values[i], 0, len(array_Y))
    plt.plot(x_values, y_values, 'g')
    plt.xlim((array_X[0], array_X[n - 1]))
    plt.ylim((array_Y[0], array_Y[n - 1]))
    plt.title('f(x)')
    plt.show()


def newton_div_difference(array_X, array_Y, given_X, start_id, end_id):
    length = end_id - start_id
    coefficient_arr = np.zeros([length, length])

    coefficient_arr[:, 0] = array_Y[start_id:end_id]

    for col in range(1, length):
        for row in range(length - col):
            coefficient_arr[row][col] = \
                (coefficient_arr[row + 1][col - 1] - coefficient_arr[row][col - 1]) / (
                        array_X[row + col + start_id] - array_X[row + start_id])

    estimated_val = 0
    for col in range(length):
        estimated_val += (coefficient_arr[0][col] * capitalPIProduct(array_X, given_X, col, start_id))

    return estimated_val


def capitalPIProduct(array_X, given_X, col, start_id):
    if col == 0:
        return 1
    product = 1
    for c in range(start_id, start_id + col):
        product *= (given_X - array_X[c])

    return product


def identifyStartEnd(array_X, given_X, order, index):
    start_id = index
    end_id = index + 2

    for x in range(order - 1):
        if start_id == 0:
            end_id += 1
        elif end_id >= len(array_X):
            start_id -= 1
        elif given_X < (array_X[start_id - 1] + array_X[end_id]) / 2:
            start_id -= 1
        else:
            end_id += 1

    return [start_id, end_id]


def validityCheck(array_X, given_X):
    if given_X < array_X[0] or given_X > array_X[len(array_X) - 1]:
        print(f"{COLORS.FAIL}The value of the given x = {given_X} is out of bounds")
        return False
    return True


def alreadyPresent(array_X, array_Y, given_X):
    for i in range(len(array_X)):
        if given_X == array_X[i]:
            print(f"{COLORS.BLUE}The value at x = {given_X} is already present and the value is: {array_Y[i]}")
            return True
    return False


def answer_function(array_X, array_Y, given_X):
    if not validityCheck(array_X, given_X) or alreadyPresent(array_X, array_Y, given_X):
        return

    old_solve = new_solve = 0
    select_id = 0
    for i in range(1, len(array_X)):
        if array_X[i - 1] < given_X < array_X[i]:
            select_id = i - 1
            break

    for i in range(1, len(array_Y)):
        [start_id, end_id] = identifyStartEnd(array_X, given_X, i, select_id)
        new_solve = newton_div_difference(array_X, array_Y, given_X, start_id, end_id)
        if i == 1:
            data_table.add_row([i, new_solve, "--"])
        else:
            new_err = math.fabs((new_solve - old_solve) / new_solve) * 100
            data_table.add_row([i, new_solve, new_err])

        old_solve = new_solve

    print()
    print(f"{COLORS.HEADER}The estimated value at x = {given_X} is: {new_solve}")
    print(f"{COLORS.RESET}{data_table}")


if __name__ == "__main__":
    x_arr = np.array([0, 10, 15, 20, 22.5, 30])
    y_arr = np.array([0, 227.04, 362.78, 517.35, 602.97, 901.67])
    # x_arr = np.array([3, 7, 11, 19])
    # y_arr = np.array([42, 43, 47, 60])
    draw_graph(x_arr, y_arr)
    x_val = float(input())
    answer_function(x_arr, y_arr, x_val)
