from utils.Integration import *
from utils.Draw_graph import *


def getSum(arr):
    sum = 0.0
    for i in range(len(arr)):
        sum += arr[i]

    return sum


def special_linear_regression(x_arr, y_arr):
    summationXY = getSum(x_arr * y_arr)
    summationX2 = getSum(x_arr ** 2)

    a1 = (summationXY / summationX2)

    print(f"\n{COLORS.HEADER}For Special linear regression:\n {COLORS.RESET}a1 : {a1 * 1e-9}\n")
    integral(0, a1 * 1e-9)
    draw_linear(0, a1)
