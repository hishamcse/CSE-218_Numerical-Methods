import math

from prettytable import PrettyTable

from Differentiation import *
from Draw_Graph import *
from Helpers import *


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
    print(f"{COLORS.HEADER}The estimated {ans_type} at t = {given_X} is: {new_solve}")
    print(f"{COLORS.RESET}{data_table}")

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
    velocity = answer_function(x_arr, y_arr_velocity, t, degree, 'velocity')

    draw_graph(x_arr, y_arr_mass, t, mass, 'mass')
    draw_graph(x_arr, y_arr_velocity, t, velocity, 'velocity')

    differentiate(x_arr, y_arr_mass, y_arr_velocity, t, degree)
