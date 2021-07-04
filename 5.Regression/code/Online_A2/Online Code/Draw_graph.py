import matplotlib.pyplot as plt
import numpy as np


def initialize():
    plt.title("Regression Plots")
    plt.minorticks_on()
    plt.xlabel('X')
    plt.ylabel('Y')


def draw_given_points(array_X, array_Y):
    initialize()
    plt.plot(array_X, array_Y, 'b.', markersize=5, label="Given Points")


def draw_curve(arr, color):
    X = np.linspace(0, 4, 50)
    Y = np.zeros(len(X))
    for i in range(len(X)):
        Y[i] = (arr[0] * (X[i] ** 2)) / (arr[1] + (X[i] ** 2))
    plt.plot(X, Y, color, label=f"Hybrid Regression")


def show_graph():
    plt.legend()
    plt.show()
