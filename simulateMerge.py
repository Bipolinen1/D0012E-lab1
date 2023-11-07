import time
import random
from bMergeSort import *
from iMergeSort import *
from iterBMergeSort import *


def simulateMerge(nr_k, runs_per_k):
    times = []
    total_time = 0
    for k in range(1,nr_k):
        for j in range(runs_per_k):
            data = random.sample(range(1, 10000000), 100000)
            start_time = time.time()
            bMergeSort(data, k)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/runs_per_k

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0
    return times

