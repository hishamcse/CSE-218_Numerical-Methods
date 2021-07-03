import math

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
    X = np.linspace(0, 2, 50)
    Y = np.zeros(len(X))
    for i in range(len(X)):
        Y[i] = arr[0] * X[i] + arr[1] * math.exp(X[i])
    plt.plot(X, Y, color, label=f"Hybrid Model Regression")


def show_graph():
    plt.legend()
    plt.show()
