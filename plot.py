import matplotlib.pyplot as plt


def plotter(time, k):
    plt.plot(time, k)
    plt.ylabel(time)
    plt.xlabel(k)
    plt.show()
