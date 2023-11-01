from bMergeSort import *
from iMergeSort import *
import time
import random

list1 = random.sample(range(-10000, 10000), 1000)
startTime = time.time()
print(bMergeSort(list1, 2))
endTime = time.time()
print(endTime-startTime)
startTime = time.time()
print(iMergeSort(list1, 2))
endTime = time.time()
print(endTime-startTime)
