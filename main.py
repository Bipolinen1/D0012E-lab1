from bMergeSort import *
from iMergeSort import *
from iterBMergeSort import *
import time
import random

list1 = random.sample(range(-100000, 1000001), 100000)
"""
startTime = time.time()
print(bMergeSort(list1, 2))
endTime = time.time()
print(endTime-startTime)
startTime = time.time()
print(iMergeSort(list1, 2))
endTime = time.time()
print(endTime-startTime)

for i in range(2, 11):
    list2 = [8, 7, 6, 5, 2, 9, 10, 12, -3, 78, -13, 3, 4, 5, 65]
    print(bMergeSort(list2, i))"""

startTime = time.time()
print(iterBSort(list1))
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
