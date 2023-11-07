from bMergeSort import *
from iMergeSort import *
from iterBMergeSort import *
import time
import random

list1 = random.sample(range(-100000, 1000001), 100000)


startTime = time.time()
print(bMergeSort(list1, 4))
endTime = time.time()
print(endTime-startTime)

"""totalTime = 0
bestTime = 10000
for i in range(1, 100):
    for j in range(10):
        ls = random.sample(range(-1000000, 10000001), 100000)
        startTime = time.time()
        bMergeSort(ls, i)
        endTime = time.time()
        totalTime += startTime - endTime
    print(totalTime)
    if totalTime < bestTime:
        bestTime = totalTime
print(bestTime)"""
