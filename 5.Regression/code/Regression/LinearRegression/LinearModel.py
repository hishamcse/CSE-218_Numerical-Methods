from utils.Differentiation import *
from utils.Integration import *
from utils.Draw_graph import *


def getSum(arr):
    sum = 0.0
    for i in range(len(arr)):
        sum += arr[i]

    return sum


def linear_calculation(x_arr, y_arr):
    size = len(x_arr)
    summationXY = getSum(x_arr * y_arr)
    summationX = getSum(x_arr)
    summationY = getSum(y_arr)
    summationX2 = getSum(x_arr ** 2)

    yBar = summationY / size
    xBar = summationX / size

    a1 = (size * summationXY - summationX * summationY) / (size * summationX2 - summationX ** 2)
    a0 = yBar - a1 * xBar

    return a0, a1


def linear_regression(x_arr, y_arr):
    a0, a1 = linear_calculation(x_arr, y_arr)

    print(f"\n{COLORS.HEADER}For linear regression:\n {COLORS.RESET}a0 : {a0} \n a1 : {a1}")
    differential("linear", a0, a1)
    integral("linear", a0, a1)
    draw_linear(a0, a1)
