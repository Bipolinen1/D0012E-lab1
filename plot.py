import matplotlib.pyplot as plt


def plotter(k, time, name):
    save = name + ".pdf"
    plt.plot(time, k, label=name)
    plt.ylabel("Time")
    plt.xlabel("k")
    plt.legend()
    plt.savefig(save)
