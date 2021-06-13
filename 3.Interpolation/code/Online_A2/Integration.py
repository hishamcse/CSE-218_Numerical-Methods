from sympy import *
from Helpers import *
from Newton_Div_Diff import *


def build_function(array_X, array_Y, unknown_X, given_X, order):
    [start_id, end_id] = identifyStartEnd(array_X, given_X, order, initialStart(array_X, given_X))
    new_solve = newton_div_difference(array_X, array_Y, unknown_X, start_id, end_id)

    return new_solve


def integral(x_arr, y_arr, volumes, order):
    x = Symbol('x')
    func_ab = build_function(x_arr[0], y_arr[0], x, volumes[0], order)
    func_bc = build_function(x_arr[1], y_arr[1], x, volumes[1], order)

    integral_ab = integrate(func_ab, (x, 25, 30))
    integral_bc = integrate(func_bc, (x, 30, 35))
    total_work = integral_ab + integral_bc

    print()
    print(f"{COLORS.HEADER}The estimated total work between v=25 and v=35 cubic m is: {total_work} J")
