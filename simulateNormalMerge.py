import time
import random
from normalMerge import *


def simulateNormalMerge(nr_k, runs_per_k, n):
    nsort_times = []
    total_time = 0
    for k in range(1,nr_k):
        for j in range(runs_per_k):
            data = random.sample(range(1, n+1), n)
            start_time = time.time()
            mergeSort(data)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/runs_per_k

        print('x:', k)
        print('y:', avg_time)

        nsort_times.append(avg_time)
        total_time = 0

    best_time = min(nsort_times)
    print(f'best time: {best_time} with k = {nsort_times.index(best_time)+1}')
    return nsort_times
