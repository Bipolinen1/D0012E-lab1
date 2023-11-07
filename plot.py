import matplotlib.pyplot as plt


def plotter(k, time):
    plt.plot(time, k)
    plt.ylabel("Time")
    plt.xlabel("k")
    plt.show()
