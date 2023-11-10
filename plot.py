import matplotlib.pyplot as plt


def plotter(k, time, name):
    save = name + ".pdf"
    plt.plot(time, k, label=name)
    plt.ylabel("Time")
    plt.xlabel("k")
    plt.legend()
    plt.savefig(save)


def nPlotter(n_list,time, name):
    save = name + ".pdf"
    plt.plot(time, n_list, label=name)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.legend()
    plt.savefig(save)
