"""
Created on Saturday May 29 11:15:41 2021

@author: Syed Jarullah Hisham
         Roll: 1805004
         CSE '18 Section A1
"""
import math


def func(h):
    return (h ** 3) - (9 * (h ** 2)) + (12 / math.pi)


def method_bisection(low, high, approx_err, max_iter):
    new_mid = 0
    old_mid = 0
    for i in range(max_iter):
        new_mid = (low + high) / 2
        if i != 0:
            new_err = math.fabs((new_mid - old_mid) / new_mid) * 100
            if new_err < approx_err:
                return new_mid

        if func(low) * func(new_mid) < 0:
            high = new_mid
        elif func(low) * func(new_mid) > 0:
            low = new_mid
        else:
            return new_mid
        old_mid = new_mid

    return new_mid


if __name__ == "__main__":
    print("root of the eqn: ", method_bisection(0, 3, .5, 20))
