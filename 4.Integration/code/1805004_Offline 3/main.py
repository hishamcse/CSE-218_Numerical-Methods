from simpson import simpson_result
from trapezoid import trapezoid_result

if __name__ == "__main__":
    print('Enter the value of subIntervals:')
    subIntervals = int(input())
    t0 = 8
    t1 = 30
    trapezoid_result(t0, t1, subIntervals)
    simpson_result(t0, t1, 2 * subIntervals)
