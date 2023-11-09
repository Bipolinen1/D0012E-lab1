import matplotlib.pyplot as plt


def plotter(k, time):
    plt.plot(time, k)
    plt.ylabel("Time")
    plt.xlabel("k")
    plt.show()

def nPlotter(n_list,time):
    plt.plot(time, n_list)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.show()