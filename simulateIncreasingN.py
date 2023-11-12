from bMergeSort import *
from iMergeSort import *
from normalMerge import *
from iterBMergeSort import iterBMergeSort
from iterBSort import *
from insertionSort import *
import random
import time


def simulateIncreasingNBMerge():
    times = []
    total_time = 0
    for k in range(10000, 200001, 10000):
        for j in range(100):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            bMergeSort(data, 32)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/100

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times


def simulateIncreasingNIterBMerge():
    times = []
    total_time = 0
    for k in range(10000, 1010000, 100000):
        for j in range(100):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            iterBMergeSort(data, 136)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/100

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times


def simulateIncreasingNIMerge():
    times = []
    total_time = 0
    for k in range(10000, 1010000, 100000):
        for j in range(100):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            iMergeSort(data, 13)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/100

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times


def simulateIncreasingNNormalMerge():
    times = []
    total_time = 0
    for k in range(10000, 1010000, 100000):
        for j in range(100):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            mergeSort(data)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/100

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times


def simulateIncreasingNBSort():
    times = []
    total_time = 0
    for k in range(10000, 200001, 10000):
        for j in range(5):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            bSort(data)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/100

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times


def simulateIncreasingNIterBSort():
    times = []
    total_time = 0
    for k in range(10000, 200001, 10000):
        for j in range(5):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            iterBSort(data)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/100

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times


def simulateIncreasingNISort():
    times = []
    total_time = 0
    for k in range(10000, 50001, 10000):
        for j in range(5):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            insertionSort(data)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/100

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times
