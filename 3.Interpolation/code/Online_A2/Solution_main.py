import math

from prettytable import PrettyTable

from Draw_Graph import *
from Integration import *


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

    integral([x_arr_volume1, x_arr_volume2], [y_arr_pressure1, y_arr_pressure2], [v1, v2], degree)
