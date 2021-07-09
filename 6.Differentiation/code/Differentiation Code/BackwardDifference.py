from utils import *


def backward_diff_formula(x, delx):
    return (func(x) - func(x - delx)) / delx


def backward_diff_result(x, delx):
    true_val = true_diff(x)
    calculated_val = backward_diff_formula(x, delx)
    print(f"{COLORS.HEADER}\nGenerating result using Backward Difference Approximation:\n")
    print(f"{COLORS.RESET}True diff is : {true_val}")
    print(f"Differentiation using backward difference is : {calculated_val}")
    print(f"Absolute relative true error : {relative_true_error(true_val, calculated_val)} %")
