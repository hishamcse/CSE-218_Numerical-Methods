import matplotlib.pyplot as plt
import numpy as np

from utils.helpers import *


def initialize():
    # plt.figure(figsize=(8, 6))
    plt.title("Regression Plots")
    plt.minorticks_on()
    plt.xlabel('X')
    plt.ylabel('Y')
    # plt.xlim((0, 12))
    # plt.ylim((-1, 25))


def draw_given_points(array_X, array_Y):
    initialize()
    plt.plot(array_X, array_Y, 'b.', markersize=2, label="Given Points")


def draw_linear(*argv):
    X = np.linspace(0, 12, 101)
    Y = linearFunc(argv[0], argv[1], X)
    plt.plot(X, Y, 'g', label="Linear Regression")


def draw_exponent(*argv):
    X = np.linspace(0, 12, 101)
    Y = np.zeros(len(X))
    for i in range(len(X)):
        Y[i] = exponentFunc(argv[0], argv[1], X[i])
    plt.plot(X, Y, 'r', label="Exponential Regression")


def draw_polynomial(arr):
    X = np.linspace(0, 12, 101)
    Y = polynomialFunc(arr, X)
    plt.plot(X, Y, 'orange', label=f"{len(arr) - 1} Order Polynomial Regression")


def show_graph():
    plt.legend()
    plt.show()
