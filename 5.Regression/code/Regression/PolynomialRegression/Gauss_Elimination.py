import math

EPSILON = 1e-8
noOfRows = 0
noOfCols = 0


def GaussianElimination(arr_A, arr_B):
    global noOfRows, noOfCols
    noOfRows = len(arr_A)
    noOfCols = len(arr_A[0])
    forward_elimination(arr_A, arr_B)
    return back_substitution(arr_A, arr_B)


def forward_elimination(arr_A, arr_B):
    global noOfRows, noOfCols
    for pivot in range(noOfRows):
        maxR = pivot
        for row in range(pivot + 1, noOfRows):
            if math.fabs(arr_A[row][pivot]) > math.fabs(arr_A[maxR][pivot]):
                maxR = row

        swap(arr_A, arr_B, pivot, maxR)

        if math.fabs(arr_A[pivot][pivot]) == 0:
            continue

        x = arr_A[pivot][pivot]
        for row in range(pivot + 1, noOfRows):
            y = arr_A[row][pivot]
            alpha = (y / x)
            for col in range(pivot, noOfCols):
                arr_A[row][col] = (arr_A[row][col] - (alpha * arr_A[pivot][col]))
            arr_B[row][0] = arr_B[row][0] - (alpha * arr_B[pivot][0])


def swap(arr_A, arr_B, r1, r2):
    temp_row = arr_A[r1]
    arr_A[r1] = arr_A[r2]
    arr_A[r2] = temp_row
    temp_row = arr_B[r1]
    arr_B[r1] = arr_B[r2]
    arr_B[r2] = temp_row


def back_substitution(arr_A, arr_B):
    global noOfRows, noOfCols
    ans = [0 for _ in range(noOfRows)]
    for i in range(noOfRows - 1, -1, -1):
        sum = 0.0
        for j in range(i + 1, noOfCols):
            sum += arr_A[i][j] * ans[j]

        if math.fabs(arr_A[i][i]) <= EPSILON:
            return None
        else:
            ans[i] = (arr_B[i][0] - sum) / arr_A[i][i]

    return ans
