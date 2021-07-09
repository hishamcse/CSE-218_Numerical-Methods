import math
from sympy import *


class COLORS:
    RESET = '\033[0m'
    HEADER = '\033[96m'
    BLUE = '\033[94m'
    FAIL = '\033[91m'


def func(x):
    return 2000 * math.log(14e4 / (14e4 - 2100 * x)) - 9.8 * x


def symbol_func(x):
    return 2000 * log(14e4 / (14e4 - 2100 * x)) - 9.8 * x


def true_diff(t):
    x = Symbol('x')
    function = symbol_func(x)
    diff_func = function.diff(x)
    diff_lambda = lambdify(x, diff_func)
    return diff_lambda(t)


def true_double_diff(t):
    x = Symbol('x')
    function = symbol_func(x)
    diff_func = function.diff(x)
    diff_lambda = lambdify(x, diff_func.diff(x))
    return diff_lambda(t)


def relative_true_error(true_val, calc_val):
    return (math.fabs(true_val - calc_val) / true_val) * 100
