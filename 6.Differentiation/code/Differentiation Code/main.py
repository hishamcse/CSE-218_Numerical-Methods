from ForwardDifference import *
from BackwardDifference import *
from CentralDifference import *
from HigherOrder import *

if __name__ == "__main__":
    x = float(input())
    delx = float(input())
    forward_diff_result(x, delx)
    backward_diff_result(x, delx)
    central_diff_result(x, delx)
    secondOrder_forward_diff_result(x, delx)
    secondOrder_central_diff_result(x, delx)
