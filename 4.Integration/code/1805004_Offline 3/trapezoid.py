from utils import COLORS, func, generate_table


def apply_trapezoid(low, high, n):
    segment_width = (high - low) / n  # determine h
    sum_area = 0.5 * (func(low) + func(high))
    for i in range(1, n):
        sum_area += func(low + segment_width * i)

    return sum_area * segment_width


def trapezoid_result(lower_limit, higher_limit, subIntervals):
    print(COLORS.BLUE, "\n--------Generating result using trapezoid rule--------\n")
    result = apply_trapezoid(lower_limit, higher_limit, subIntervals)
    print(f"{COLORS.RESET}Distance covered from t = {lower_limit} to t = {higher_limit} is: {result}")
    generate_table(lower_limit, higher_limit, apply_trapezoid)
