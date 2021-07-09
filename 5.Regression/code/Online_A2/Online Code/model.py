from Draw_graph import *


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


def calculation(arr_X, arr_Y):
    temp_arr = linear_calculation(1 / (arr_X ** 2), 1 / arr_Y)
    ans_arr = [1 / temp_arr[0], temp_arr[1] / temp_arr[0]]
    print(f"Kmax:{ans_arr[0]} Cs:{ans_arr[1]}")
    draw_curve(ans_arr, 'red')
