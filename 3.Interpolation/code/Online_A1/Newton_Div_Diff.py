import numpy as np


def newton_div_difference(array_X, array_Y, given_X, start_id, end_id):
    length = end_id - start_id
    coefficient_arr = np.zeros([length, length])

    coefficient_arr[:, 0] = array_Y[start_id:end_id]

    for col in range(1, length):
        for row in range(length - col):
            coefficient_arr[row][col] = \
                (coefficient_arr[row + 1][col - 1] - coefficient_arr[row][col - 1]) / (
                        array_X[row + col + start_id] - array_X[row + start_id])

    estimated_val = 0
    for col in range(length):
        estimated_val += (coefficient_arr[0][col] * capitalPIProduct(array_X, given_X, col, start_id))

    return estimated_val


def capitalPIProduct(array_X, given_X, col, start_id):
    if col == 0:
        return 1
    multiplication = 1
    for c in range(start_id, start_id + col):
        multiplication *= (given_X - array_X[c])

    return multiplication
