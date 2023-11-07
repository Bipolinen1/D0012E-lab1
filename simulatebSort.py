import time
import random
from bMergeSort import *
from iMergeSort import *
from iterBMergeSort import *
from bSort import *


def simulatebSort():
    total_time = 0

    for i in range(10):
        data = random.sample(range(1, 10000000), 100000)
        start_time = time.time()
        bSort()

