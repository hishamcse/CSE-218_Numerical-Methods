"""
Created on Tuesday Mar 30 16:12:41 2021

@author: Syed Jarullah Hisham
         Roll: 1805004
         CSE '18 Section A1
"""
import math

EPSILON = 1e-8
noOfRows = 0
noOfCols = 0


def GaussianElimination(arr_A, arr_B, d=True):
    global noOfRows, noOfCols
    noOfRows = len(arr_A)
    noOfCols = len(arr_A[0])
    forward_elimination(arr_A, arr_B, d)
    return back_substitution(arr_A, arr_B)


def forward_elimination(arr_A, arr_B, d):
    global noOfRows, noOfCols
    for pivot in range(noOfRows):
        maxR = pivot
        for row in range(pivot + 1, noOfRows):
            if math.fabs(arr_A[row][pivot]) > math.fabs(arr_A[maxR][pivot]):
                maxR = row

        swap(arr_A, arr_B, pivot, maxR)

        if math.fabs(arr_A[pivot][pivot] == 0):
            continue

        x = arr_A[pivot][pivot]
        for row in range(pivot + 1, noOfRows):
            y = arr_A[row][pivot]
            alpha = (y / x)
            for col in range(pivot, noOfCols):
                arr_A[row][col] = (arr_A[row][col] - (alpha * arr_A[pivot][col]))
            arr_B[row][0] = arr_B[row][0] - (alpha * arr_B[pivot][0])
            if d:
                print_Matrix(arr_A, arr_B)


def swap(arr_A, arr_B, r1, r2):
    temp_row = arr_A[r1]
    arr_A[r1] = arr_A[r2]
    arr_A[r2] = temp_row
    temp_row = arr_B[r1]
    arr_B[r1] = arr_B[r2]
    arr_B[r2] = temp_row


def print_Matrix(A, B):
    print("\nA = ")
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(format(A[i][j], ".4f"), end=" ")
        print()
    print("B = ")
    for i in range(len(B)):
        print(format(B[i][0], ".4f"))


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


if __name__ == "__main__":
    n = int(input())
    arr_A = [[0 for i in range(n)] for j in range(n)]
    arr_B = [[0] for i in range(n)]

    for i in range(n):
        str = input().split(" ")
        for j in range(n):
            arr_A[i][j] = float(str[j])
    print()
    for i in range(n):
        str = input()
        arr_B[i][0] = float(str)

    ans = GaussianElimination(arr_A, arr_B)
    if ans is None:
        print("\nNo Solution or Infinite solution")
    else:
        print()
        for i in range(n):
            print(format(ans[i] + 0, ".4f"))
