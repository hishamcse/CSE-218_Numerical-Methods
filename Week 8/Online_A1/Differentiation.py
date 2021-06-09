from sympy import *
from Newton_Div_Diff import *
from Helpers import *


def build_function(array_X, array_Y, unknown_X, given_X, order):
    [start_id, end_id] = identifyStartEnd(array_X, given_X, order, initialStart(array_X, given_X))
    new_solve = newton_div_difference(array_X, array_Y, unknown_X, start_id, end_id)

    return new_solve


def differentiate(x_arr, y_arr_mass, y_arr_velocity, t, order):
    x = Symbol('x')
    func_mass = build_function(x_arr, y_arr_mass, x, t, order)
    func_velocity = build_function(x_arr, y_arr_velocity, x, t, order)

    momentum_func = func_mass * func_velocity
    force = momentum_func.diff(x)
    force_func = lambdify(x, force)
    print()
    print(f"{COLORS.HEADER}The estimated total applied force at t = {t} is: {force_func(t)}")
