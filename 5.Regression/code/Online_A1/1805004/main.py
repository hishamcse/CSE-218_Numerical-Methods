from model import *
from Draw_graph import *

if __name__ == "__main__":
    f = open('data.txt', 'r')
    Lines = f.readlines()
    size = len(Lines)
    x_arr = np.zeros(size)
    y_arr = np.zeros(size)

    for lineNo in range(size):
        str = Lines[lineNo].split(' ')
        x_arr[lineNo] = float(str[0])
        y_arr[lineNo] = float(str[1])
    f.close()

    draw_given_points(x_arr, y_arr)

    calculation(np.copy(x_arr), np.copy(y_arr))

    show_graph()
