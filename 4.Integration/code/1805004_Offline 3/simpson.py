from utils import COLORS, func, generate_table


def single_simpson(low, mid, high):
    return ((high - low) / 2) * (func(low) + (4 * func(mid)) + func(high))


def apply_simpson(low, high, n):
    segment_width = (high - low) / n  # determine h
    sum = 0
    start = low
    for i in range(1, n + 1, 2):
        sum += single_simpson(start, low + segment_width * i, low + segment_width * (i + 1))
        start = low + segment_width * (i + 1)
    return (1.0 / 3.0) * sum


def simpson_result(lower_limit, higher_limit, subIntervals):
    print(COLORS.BLUE, "\n--------Generating result using simpson's 1/3 rule--------\n")
    result = apply_simpson(lower_limit, higher_limit, subIntervals)
    print(f"{COLORS.RESET}Distance covered from t = {lower_limit} to t = {higher_limit} is: {result}")
    generate_table(lower_limit, higher_limit, apply_simpson, True)
