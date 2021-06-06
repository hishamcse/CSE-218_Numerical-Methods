import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from prettytable import PrettyTable
import math


class COLORS:
    RESET = '\033[0m'
    HEADER = '\033[96m'
    BLUE = '\033[94m'
    FAIL = '\033[91m'


def draw_individual_graph(array_X, array_Y, given_X, value):
    arrow_properties = dict(
        facecolor="black", width=0.5,
        headwidth=10, shrink=1)

    plt.plot(array_X, array_Y, 'g')

    plt.annotate(f"({given_X}, {value})", (given_X, value), color='b', arrowprops=arrow_properties)
    plt.title('pressure vs volume')


def draw_AllGraphs(arrays_X, arrays_Y, givens_X, values):
    fig, ax = plt.subplots()
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    plt.grid(b=True, which='major', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', linestyle='-', alpha=0.3)
    plt.margins(x=0, y=0)
    plt.xlabel('volume(V)')
    plt.ylabel('pressure(P)')
    plt.xlim((0, 45))
    plt.ylim((0, 70))
    draw_individual_graph(arrays_X[0], arrays_Y[0], givens_X[0], values[0])
    draw_individual_graph(arrays_X[1], arrays_Y[1], givens_X[1], values[1])
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
    multiplication = 1
    for c in range(start_id, start_id + col):
        multiplication *= (given_X - array_X[c])

    return multiplication


def initialStart(array_X, given_X):
    for i in range(1, len(array_X)):
        if array_X[i - 1] < given_X < array_X[i]:
            return i - 1


def identifyStartEnd(array_X, given_X, order, index):
    start_id = index
    end_id = index + 2

    for _ in range(order - 1):
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


def answer_function(array_X, array_Y, given_X, order, ans_type):
    if not validityCheck(array_X, given_X) or alreadyPresent(array_X, array_Y, given_X):
        return

    old_solve = new_solve = 0
    select_id = initialStart(array_X, given_X)

    data_table = PrettyTable()
    data_table.field_names = ["order of polynomial", f"{ans_type}", "error%"]

    for i in range(1, order + 1):
        [start_id, end_id] = identifyStartEnd(array_X, given_X, i, select_id)
        new_solve = newton_div_difference(array_X, array_Y, given_X, start_id, end_id)
        if i == 1:
            data_table.add_row([i, new_solve, "--"])
        else:
            new_err = math.fabs((new_solve - old_solve) / new_solve) * 100
            data_table.add_row([i, new_solve, new_err])

        old_solve = new_solve

    print()
    print(f"{COLORS.HEADER}The estimated pressure at v = {given_X} cubic m is: {new_solve} pascal")
    print(f"{COLORS.RESET}{data_table}")

    return new_solve


def build_function(array_X, array_Y, unknown_X, given_X, order):
    [start_id, end_id] = identifyStartEnd(array_X, given_X, order, initialStart(array_X, given_X))
    new_solve = newton_div_difference(array_X, array_Y, unknown_X, start_id, end_id)

    return new_solve


if __name__ == "__main__":
    f = open('pressure.txt', 'r')
    Lines = f.readlines()
    size = 0
    for lineNo in range(1, len(Lines)):
        if Lines[lineNo].split('\t')[0] == '30':
            size = lineNo
            break
    x_arr_volume1 = np.zeros(size)
    x_arr_volume2 = np.zeros(len(Lines) - size)
    y_arr_pressure1 = np.zeros(size)
    y_arr_pressure2 = np.zeros(len(Lines) - size)

    for lineNo in range(1, len(Lines)):
        if lineNo < size:
            x_arr_volume1[lineNo - 1] = float(Lines[lineNo].split('\t')[0])
            y_arr_pressure1[lineNo - 1] = float(Lines[lineNo].split('\t')[1])
        elif lineNo == size:
            x_arr_volume1[lineNo - 1] = float(Lines[lineNo].split('\t')[0])
            x_arr_volume2[lineNo - size] = float(Lines[lineNo].split('\t')[0])
            y_arr_pressure1[lineNo - 1] = float(Lines[lineNo].split('\t')[1])
            y_arr_pressure2[lineNo - size] = float(Lines[lineNo].split('\t')[1])
        else:
            x_arr_volume2[lineNo - size] = float(Lines[lineNo].split('\t')[0])
            y_arr_pressure2[lineNo - size] = float(Lines[lineNo].split('\t')[1])
    f.close()

    v1 = 28
    v2 = 32
    degree = 3

    pressure_ab = answer_function(x_arr_volume1, y_arr_pressure1, v1, degree, 'pressure_ab')
    pressure_bc = answer_function(x_arr_volume2, y_arr_pressure2, v2, degree, 'pressure_bc')

    draw_AllGraphs([x_arr_volume1, x_arr_volume2], [y_arr_pressure1, y_arr_pressure2], [v1, v2],
                   [pressure_ab, pressure_bc])

    x = Symbol('x')
    func_ab = build_function(x_arr_volume1, y_arr_pressure1, x, v1, degree)
    func_bc = build_function(x_arr_volume2, y_arr_pressure2, x, v2, degree)

    integral_ab = integrate(func_ab, (x, 25, 30))
    integral_bc = integrate(func_bc, (x, 30, 35))
    total_work = integral_ab + integral_bc

    print()
    print(f"{COLORS.HEADER}The estimated total work between v={v1} and v={v2} is: {total_work} J")
