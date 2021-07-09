from utils import *


def central_diff_formula(x, delx):
    return (func(x + delx) - func(x - delx)) / (2 * delx)


def central_diff_result(x, delx):
    true_val = true_diff(x)
    calculated_val = central_diff_formula(x, delx)
    print(f"{COLORS.HEADER}\nGenerating result using Central Difference Approximation:\n")
    print(f"{COLORS.RESET}True diff is : {true_val}")
    print(f"Differentiation using central difference is : {calculated_val}")
    print(f"Absolute relative true error : {relative_true_error(true_val, calculated_val)} %")
