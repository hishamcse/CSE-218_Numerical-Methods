import math

from prettytable import PrettyTable


class COLORS:
    RESET = '\033[0m'
    HEADER = '\033[96m'
    BLUE = '\033[94m'
    FAIL = '\033[91m'


def func(t):
    return 2000 * math.log(140000 / (140000 - 2100 * t)) - 9.8 * t


def generate_table(low, high, apply_rule, simpson=False):
    data_table = PrettyTable()
    data_table.field_names = ["value of n", "calculated value", "error%"]

    print(f"\n{COLORS.HEADER}Calculated values and absolute approx relative errors for n = 1 to 5")

    old_solve = 0
    for i in range(1, 6):
        if simpson:
            new_solve = apply_rule(low, high, 2 * i)
        else:
            new_solve = apply_rule(low, high, i)
        new_err = math.fabs((new_solve - old_solve) / new_solve) * 100
        if i == 1:
            data_table.add_row([i, new_solve, "--"])
        else:
            data_table.add_row([i, new_solve, new_err])
        old_solve = new_solve

    print(f"{COLORS.RESET}{data_table}")
