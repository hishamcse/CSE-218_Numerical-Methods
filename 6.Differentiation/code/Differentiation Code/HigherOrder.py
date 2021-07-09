from utils import *


def forward_diff_secondOrder(x, delx):
    return (func(x + 2 * delx) - 2 * func(x + delx) + func(x)) / (delx ** 2)


def central_diff_secondOrder(x, delx):
    return (func(x + delx) - 2 * func(x) + func(x - delx)) / (delx ** 2)


def secondOrder_forward_diff_result(x, delx):
    true_val = true_double_diff(x)
    calculated_val = forward_diff_secondOrder(x, delx)
    print(f"{COLORS.HEADER}\nGenerating result using Second Order Forward Difference Approximation:\n")
    print(f"{COLORS.RESET}True diff is : {true_val}")
    print(f"Differentiation using forward difference is : {calculated_val}")
    print(f"Absolute relative true error : {relative_true_error(true_val, calculated_val)} %")


def secondOrder_central_diff_result(x, delx):
    true_val = true_double_diff(x)
    calculated_val = central_diff_secondOrder(x, delx)
    print(f"{COLORS.HEADER}\nGenerating result using Second Order Central Difference Approximation:\n")
    print(f"{COLORS.RESET}True diff is : {true_val}")
    print(f"Differentiation using central difference is : {calculated_val}")
    print(f"Absolute relative true error : {relative_true_error(true_val, calculated_val)} %")
