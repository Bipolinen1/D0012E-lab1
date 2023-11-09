from bMergeSort import *

import random
import time

def simulateIncreasingN():
    times = []
    total_time = 0
    for k in range(10000, 1000000, 10000):
        for j in range(100):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            bMergeSort(data, k)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/100

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times