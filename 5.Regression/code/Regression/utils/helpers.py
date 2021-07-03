import math


class COLORS:
    RESET = '\033[0m'
    HEADER = '\033[96m'
    BLUE = '\033[94m'
    FAIL = '\033[91m'


def linearFunc(a0, a1, x):
    return a0 + a1 * x


def exponentFunc(a, b, x):
    return a * math.exp(b * x)


def polynomialFunc(arr, x):
    func = arr[0]
    for i in range(1, len(arr)):
        func = func + arr[i] * (x ** i)
    return func
