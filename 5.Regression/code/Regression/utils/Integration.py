from sympy import *
from utils.helpers import *


def integral(reg_type="linear", *argv):
    x = Symbol('x')
    if reg_type == "linear":
        func = linearFunc(argv[0], argv[1], x)
    elif reg_type == "exponent":
        func = argv[0] * exp(argv[1] * x)
    else:
        func = polynomialFunc(argv[0], x)

    integralVal = integrate(func, (x, 0, math.pi))

    print(f"{COLORS.HEADER}The estimated total energy of spring is: {integralVal} J")
