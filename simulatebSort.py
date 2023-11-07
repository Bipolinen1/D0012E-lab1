import time
import random
from bMergeSort import *
from iMergeSort import *
from iterBMergeSort import *
from bSort import *


def simulatebSort(runs, n):
    total_time = 0

    for i in range(runs):
        data = random.sample(range(1, n+1), n)
        start_time = time.time()
        bSort(data)
        end_time = time.time()
        delta_time = end_time - start_time
        total_time = total_time + delta_time

    avg_time = total_time/runs
    return avg_time


