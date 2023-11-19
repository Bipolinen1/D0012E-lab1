from bMergeSort import *
from iMergeSort import *
from normalMerge import *
from iterBMergeSort import iterBMergeSort
from bSort import *
from iterBSort import *
from insertionSort import *
import random
import time


def simulateIncreasingNBMerge():
    times = []
    total_time = 0
    counter = 1
    for k in range(100000, 1100000, 100000):
        for j in range(10):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            bMergeSort(data, 86 * counter)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/10
        counter += 1
        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times


def simulateIncreasingNIterBMerge():
    times = []
    total_time = 0
    counter = 1
    for k in range(100000, 1100000, 100000):
        for j in range(100):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            iterBMergeSort(data, 102 * counter)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/100
        counter += 1
        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times


def simulateIncreasingNIMerge():
    times = []
    total_time = 0
    counter = 1
    for k in range(100000, 1100000, 100000):
        for j in range(100):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            iMergeSort(data, 21 * counter)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/100
        counter += 1

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times


def simulateIncreasingNNormalMerge():
    times = []
    total_time = 0
    for k in range(100000, 1100000, 100000):
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
    for k in range(10000, 110001, 10000):
        for j in range(10):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            bSort(data)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/10

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times


def simulateIncreasingNIterBSort():
    times = []
    total_time = 0
    for k in range(10000, 110001, 10000):
        for j in range(10):
            data = random.sample(range(1, k+1), k)
            start_time = time.time()
            iterBSort(data)
            end_time = time.time()
            delta_time = end_time - start_time
            total_time = total_time + delta_time
        avg_time = total_time/10

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times


def simulateIncreasingNInsertionSort():
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
        avg_time = total_time/5

        print('x:', k)
        print('y:', avg_time)

        times.append(avg_time)
        total_time = 0

    return times
