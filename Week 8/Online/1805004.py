import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import math


class COLORS:
    RESET = '\033[0m'
    HEADER = '\033[96m'
    BLUE = '\033[94m'
    FAIL = '\033[91m'


def draw_graph(array_X, array_Y):
    fig, ax = plt.subplots()
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    plt.grid(b=True, which='major', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', linestyle='-', alpha=0.3)
    plt.margins(x=0, y=0)
    n = len(array_X)

    x_values = np.linspace(array_X[0], array_X[n - 1], 30)
    y_values = np.zeros(30)
    for i in range(len(x_values)):
        y_values[i] = newton_div_difference(array_X, array_Y, x_values[i], 0, len(array_Y))
    plt.plot(x_values, y_values, 'g')
    plt.xlim((array_X[0], array_X[n - 1]))
    plt.ylim((0, array_Y[n - 1] + 450))
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
    error = np.zeros(3)

    for i in range(1, order + 1):
        [start_id, end_id] = identifyStartEnd(array_X, given_X, i, select_id)
        new_solve = newton_div_difference(array_X, array_Y, given_X, start_id, end_id)
        if i != 1:
            new_err = math.fabs((new_solve - old_solve) / new_solve) * 100
            error[i - 2] = new_err

        old_solve = new_solve

    print()
    print(f"{COLORS.HEADER}The estimated {ans_type} at t = {given_X} is: {new_solve}")
    for i in range(len(error)):
        print(f"{COLORS.RESET}The absolute approximate relative error for {i + 2} order is: {error[i]}")

    return new_solve


def build_function(array_X, array_Y, unknown_X, given_X):
    [start_id, end_id] = identifyStartEnd(x_arr, given_X, degree, initialStart(x_arr, t))
    new_solve = newton_div_difference(array_X, array_Y, unknown_X, start_id, end_id)

    return new_solve


if __name__ == "__main__":
    f = open('mass.txt', 'r')
    Lines = f.readlines()
    size = len(Lines) - 1
    x_arr = np.zeros(size)
    y_arr_mass = np.zeros(size)
    y_arr_velocity = np.zeros(size)

    for lineNo in range(1, len(Lines)):
        x_arr[lineNo - 1] = float(Lines[lineNo].split('\t')[0])
        y_arr_mass[lineNo - 1] = float(Lines[lineNo].split('\t')[1])
    f.close()

    f = open('velocity.txt', 'r')
    Lines = f.readlines()
    for lineNo in range(1, len(Lines)):
        y_arr_velocity[lineNo - 1] = float(Lines[lineNo].split('\t')[1])
    f.close()

    t = 25
    degree = 4

    mass = answer_function(x_arr, y_arr_mass, t, degree, 'mass')
    vel = answer_function(x_arr, y_arr_velocity, t, degree, 'velocity')

    draw_graph(x_arr, y_arr_mass)
    draw_graph(x_arr, y_arr_velocity)

    x = Symbol('x')
    func_mass = build_function(x_arr, y_arr_mass, x, t)
    func_velocity = build_function(x_arr, y_arr_velocity, x, t)

    momentum_func = func_mass * func_velocity
    force = momentum_func.diff(x)
    force_func = lambdify(x, force)
    print()
    print(f"{COLORS.HEADER}The estimated total applied force at t = {t} is: {force_func(t)}")
