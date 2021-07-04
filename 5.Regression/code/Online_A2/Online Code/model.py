from Gauss_Elimination import *
from Draw_graph import *


def calculation(arr_X, arr_Y):
    sumX4 = sumX4Y = sumX2Y2 = sumY2 = sumX2Y = 0.0
    for i in range(len(arr_X)):
        sumX4 += arr_X[i] ** 4
        sumX2Y += (arr_X[i] ** 2) * arr_Y[i]
        sumY2 += arr_Y[i] ** 2
        sumX4Y += (arr_X[i] ** 4) * arr_Y[i]
        sumX2Y2 += (arr_X[i] ** 2) * (arr_Y[i] ** 2)

    arr_A = [[0 for _ in range(2)] for _ in range(2)]
    arr_B = [[0] for _ in range(2)]
    arr_A[0][0] = sumX4
    arr_A[0][1] = -sumX2Y
    arr_A[1][0] = sumX2Y
    arr_A[1][1] = -sumY2
    arr_B[0][0] = sumX4Y - sumX2Y
    arr_B[1][0] = sumX2Y2 - sumY2

    ans_arr = GaussianElimination(arr_A, arr_B)
    print(f"a:{ans_arr[0]} b:{ans_arr[1]}")
    draw_curve(ans_arr, 'red')
