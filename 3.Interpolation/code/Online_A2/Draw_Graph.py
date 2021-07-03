import matplotlib.pyplot as plt


def draw_individual_graph(array_X, array_Y, given_X, value):
    arrow_properties = dict(
        facecolor="black", width=0.5,
        headwidth=10, shrink=1)

    plt.plot(array_X, array_Y, 'g')

    plt.annotate(f"({given_X}, {value})", (given_X, value), color='b', arrowprops=arrow_properties)
    plt.title('pressure vs volume')


def draw_AllGraphs(arrays_X, arrays_Y, givens_X, values):
    fig, ax = plt.subplots()
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    plt.grid(b=True, which='major', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', linestyle='-', alpha=0.3)
    plt.margins(x=0, y=0)
    plt.xlabel('volume(V)')
    plt.ylabel('pressure(P)')
    plt.xlim((0, 45))
    plt.ylim((0, 70))
    draw_individual_graph(arrays_X[0], arrays_Y[0], givens_X[0], values[0])
    draw_individual_graph(arrays_X[1], arrays_Y[1], givens_X[1], values[1])
    plt.show()
