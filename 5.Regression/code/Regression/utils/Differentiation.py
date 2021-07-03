from sympy import *
from utils.helpers import *


def differential(reg_type="linear", *argv):
    x = Symbol('x')
    if reg_type == "linear":
        func = linearFunc(argv[0], argv[1], x)
    elif reg_type == "exponent":
        func = argv[0] * exp(argv[1] * x)
    else:
        func = polynomialFunc(argv[0], x)

    diff_func = func.diff(x)
    diff_val = lambdify(x, diff_func)

    print(f"{COLORS.HEADER}The estimated total momentum of spring is: {diff_val(math.pi)} kgm/s")
