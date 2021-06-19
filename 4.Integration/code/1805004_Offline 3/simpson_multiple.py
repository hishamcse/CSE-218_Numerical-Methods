# not in offline (using multiple segment formula)

from utils import COLORS, func


def apply_simpson(low, high, n):
    segment_width = (high - low) / n  # determine h
    sum_area = (func(low) + func(high))  # 1/3 portions

    for i in range(1, n, 2):  # 4/3 portions
        sum_area += 4 * func(low + segment_width * i)

    for i in range(2, n - 1, 2):  # 2/3 portions
        sum_area += 2 * func(low + segment_width * i)

    return (1.0 / 3.0) * sum_area * segment_width


def simpson_result(lower_limit, higher_limit, subIntervals):
    print(COLORS.BLUE, "\n--------Generating result using simpson's 1/3 rule--------\n")
    result = apply_simpson(lower_limit, higher_limit, subIntervals)
    print(f"{COLORS.RESET}Distance covered from t = {lower_limit} to t = {higher_limit} is: {result}")
