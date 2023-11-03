from bMergeSort import *
from iMergeSort import *
import time
import random

list1 = random.sample(range(1, 100001), 10000)
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
print(bSort(list1))
endTime = time.time()
print(endTime-startTime)
