from ExponentialRegression.Bisection import *
from utils.Differentiation import *
from utils.Draw_graph import *
from utils.Integration import *


def logConversion(arr):
    new_arr = np.zeros(len(arr))
    for i in range(len(arr)):
        new_arr[i] = math.log(arr[i])
    return new_arr


def evaluate_a(arr_X, arr_Y, b):
    sumYE = sumE = 0
    for i in range(len(arr_X)):
        sumYE += (arr_Y[i] * math.exp(b * arr_X[i]))
        sumE += math.exp(2 * b * arr_X[i])

    return sumYE / sumE


def evaluate_b(arr_X, arr_Y, b):
    sumYXE = sumYE = sumE = sumXE = 0.0
    for i in range(len(arr_X)):
        sumYXE += (arr_Y[i] * arr_X[i] * math.exp(b * arr_X[i]))
        sumYE += (arr_Y[i] * math.exp(b * arr_X[i]))
        sumE += math.exp(2 * b * arr_X[i])
        sumXE += (arr_X[i] * math.exp(2 * b * arr_X[i]))

    return sumYXE - sumYE * sumXE / sumE


def exponential_regression(x_arr, y_arr):
    # using data transformation
    # lna, b = linear_calculation(x_arr, logConversion(y_arr))
    # a = math.exp(lna)

    # using bisection method
    b = method_bisection(evaluate_b, x_arr, y_arr, -.5, 1, 0.005, 50)
    a = evaluate_a(x_arr, y_arr, b)

    print(f"\n{COLORS.HEADER}For Exponential regression:\n {COLORS.RESET}a : {a} \n b : {b}")
    differential("exponent", a, b)
    integral("exponent", a, b)
    draw_exponent(a, b)
