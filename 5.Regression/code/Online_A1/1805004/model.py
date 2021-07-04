from Gauss_Elimination import *
from Draw_graph import *


def calculation(arr_X, arr_Y):
    sumX2 = sumYXE = sumYE = sumE = sumXE = 0.0
    for i in range(len(arr_X)):
        sumX2 += arr_X[i] * arr_X[i]
        sumXE += (arr_X[i] * math.exp(arr_X[i]))
        sumYXE += (arr_Y[i] * arr_X[i])
        sumE += math.exp(2 * arr_X[i])
        sumYE += (arr_Y[i] * math.exp(arr_X[i]))

    arr_A = [[0 for _ in range(2)] for _ in range(2)]
    arr_B = [[0] for _ in range(2)]
    arr_A[0][0] = sumX2
    arr_A[0][1] = sumXE
    arr_A[1][0] = sumXE
    arr_A[1][1] = sumE
    arr_B[0][0] = sumYXE
    arr_B[1][0] = sumYE

    ans_arr = GaussianElimination(arr_A, arr_B)
    print(f"a:{ans_arr[0]} b:{ans_arr[1]}")
    draw_curve(ans_arr, 'red')
