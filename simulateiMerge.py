import time
import random
from iMergeSort import *



def simulateiMerge(nr_k, runs_per_k, n):
    isort_times = []
    total_time = 0
    for k in range(1,nr_k):
        for j in range(runs_per_k):
            data = random.sample(range(1, n+1), n)
            start_time = time.time()
            iMergeSort(data, k)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/runs_per_k

        print('x:', k)
        print('y:', avg_time)

        isort_times.append(avg_time)
        total_time = 0
    best_time = min(isort_times)
    print(f'best time: {best_time} with k = {isort_times.index(best_time) + 1}')
    return isort_times
