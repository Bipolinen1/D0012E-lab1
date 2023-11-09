import time
import random
from iterBMergeSort import *


def simulateIterBMerge(nr_k, runs_per_k, n):
    iterBsort_times = []
    total_time = 0
    for k in range(1,nr_k):
        for j in range(runs_per_k):
            data = random.sample(range(1, n+1), n)
            start_time = time.time()
            iterBMergeSort(data, k)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/runs_per_k

        print('x:', k)
        print('y:', avg_time)

        iterBsort_times.append(avg_time)
        total_time = 0

    best_time = min(iterBsort_times)
    print(f'best time: {best_time} with k = {iterBsort_times.index(best_time)+1}')
    return iterBsort_times
