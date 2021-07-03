class COLORS:
    RESET = '\033[0m'
    HEADER = '\033[96m'
    BLUE = '\033[94m'
    FAIL = '\033[91m'


def validityCheck(array_X, given_X):
    if given_X < array_X[0] or given_X > array_X[len(array_X) - 1]:
        print(f"{COLORS.FAIL}The value of the given x = {given_X} is out of bounds")
        return False
    return True


def alreadyPresent(array_X, array_Y, given_X):
    for i in range(len(array_X)):
        if given_X == array_X[i]:
            print(f"{COLORS.BLUE}The value at x = {given_X} is already present and the value is: {array_Y[i]}")
            return True
    return False


def initialStart(array_X, given_X):
    for i in range(1, len(array_X)):
        if array_X[i - 1] < given_X < array_X[i]:
            return i - 1


def identifyStartEnd(array_X, given_X, order, index):
    start_id = index
    end_id = index + 2

    for _ in range(order - 1):
        if start_id == 0:
            end_id += 1
        elif end_id >= len(array_X):
            start_id -= 1
        elif given_X < (array_X[start_id - 1] + array_X[end_id]) / 2:
            start_id -= 1
        else:
            end_id += 1

    return [start_id, end_id]
