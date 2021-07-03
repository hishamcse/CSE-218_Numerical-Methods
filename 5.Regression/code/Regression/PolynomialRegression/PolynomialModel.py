from utils.Differentiation import *
from utils.Integration import *
from utils.Draw_graph import *
from PolynomialRegression.Gauss_Elimination import *


def getSum(arr):
    sum = 0.0
    for i in range(len(arr)):
        sum += arr[i]

    return sum


def poly_calculation(x_arr, y_arr, order):
    size = len(x_arr)
    temp_Arr_A = np.zeros((2 * order) + 1)
    temp_Arr_A[0] = size
    for i in range(1, len(temp_Arr_A)):
        temp_Arr_A[i] = getSum(np.copy(x_arr) ** i)

    temp_Arr_B = np.zeros(order + 1)
    for i in range(len(temp_Arr_B)):
        temp_Arr_B[i] = getSum((np.copy(x_arr) ** i) * (np.copy(y_arr)))

    arr_A = [[0 for _ in range(order + 1)] for _ in range(order + 1)]
    arr_B = [[0] for _ in range(order + 1)]
    for i in range(len(arr_A)):
        for j in range(len(arr_A[0])):
            arr_A[i][j] = temp_Arr_A[i + j]
        arr_B[i][0] = temp_Arr_B[i]

    return GaussianElimination(arr_A, arr_B)


def polynomial_regression(x_arr, y_arr, order):
    ans_arr = poly_calculation(x_arr, y_arr, order)

    print(f"\n{COLORS.HEADER}For Polynomial regression: {COLORS.RESET}")
    for i in range(len(ans_arr)):
        print(f" a{i}: {ans_arr[i]}")
    differential("polynomial", ans_arr)
    integral("polynomial", ans_arr)
    draw_polynomial(ans_arr)
