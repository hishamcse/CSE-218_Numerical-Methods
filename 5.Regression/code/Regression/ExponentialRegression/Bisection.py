import math


def method_bisection(func, x_arr, y_arr, low, high, approx_err, max_iter):
    new_mid = 0.0
    old_mid = 0.0
    for i in range(max_iter):
        new_mid = (low + high) / 2
        if i != 0:
            new_err = math.fabs((new_mid - old_mid) / new_mid) * 100
            if new_err < approx_err:
                return new_mid

        if func(x_arr, y_arr, low) * func(x_arr, y_arr, new_mid) < 0:
            high = new_mid
        elif func(x_arr, y_arr, low) * func(x_arr, y_arr, new_mid) > 0:
            low = new_mid
        else:
            return new_mid
        old_mid = new_mid

    return new_mid
