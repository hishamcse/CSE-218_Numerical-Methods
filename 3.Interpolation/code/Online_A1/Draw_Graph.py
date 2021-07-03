import matplotlib.pyplot as plt


def draw_graph(array_X, array_Y, given_X, value, graph_type):
    fig, ax = plt.subplots()
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', array_Y[0]))
    plt.grid(b=True, which='major', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', linestyle='-', alpha=0.3)
    plt.margins(x=0, y=0)
    n = len(array_X)

    arrow_properties = dict(
        facecolor="black", width=0.5,
        headwidth=10, shrink=1)

    plt.plot(array_X, array_Y, 'g')
    plt.xlabel('t')
    plt.ylabel(graph_type)
    plt.xlim((array_X[0], array_X[n - 1]))
    plt.ylim((array_Y[0], array_Y[n - 1]))
    plt.annotate(f"({given_X}, {value})", (given_X, value), color='b', arrowprops=arrow_properties)
    plt.title(f"{graph_type} vs time")
    plt.show()
