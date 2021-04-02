"""
Created on Sat Mar 27 16:12:41 2021

@author: Syed Jarullah Hisham
         Roll: 1805004
         CSE '18 Section A1
"""


def GaussianElimination(arr_A, arr_B, d=True):
    length = len(arr_A)
    row = 0
    col = 0
    for i in range(length):
        x = arr_A[row][col]
        for j in range(i+1, length):
            y = arr_A[j][col]
            for l in range(length):
                arr_A[j][l] = (arr_A[j][l]-((y/x)*arr_A[row][l]))
            arr_B[j][0] = arr_B[j][0]-((y/x)*arr_B[row][0])
            print_Matrix(arr_A, arr_B,d)
        col += 1
        row += 1


def print_Matrix(arr_A, arr_B, d=True):
    print("\nA = ")
    if d:
        length = len(arr_A)
        for i in range(length):
            for j in range(length):
                print(format(arr_A[i][j],".4f"), end=" ")
            print()
    print("B = ")
    for i in range(len(arr_B)):
        print(format(arr_B[i][0],".4f"))


if __name__ == "__main__":
    n = int(input())
    arr_A = [[0 for i in range(n)] for j in range(n)]
    arr_B = [[0] for i in range(n)]

    for i in range(n):
        str = input().split(" ")
        for j in range(n):
            arr_A[i][j] = float(str[j])

    for i in range(n):
        str = input()
        arr_B[i][0] = float(str)

    GaussianElimination(arr_A, arr_B)
