import random
import time

from bMergeSort import *
from iMergeSort import *
from iterBMergeSort import *
from plot import *
from simulateIncreasingN import *
from simulatebMerge import *
from simulateIterBMerge import *
from simulateiMerge import *
from simulateNormalMerge import *
from simulateiMerge import *
from testBmerge import  *
"""plotter(simulatebMerge(200, 200, 100000), range(1, 200), "bMerge")
plotter(simulateIterBMerge(200, 200, 100000), range(1, 200), "iterBMerge")
plotter(simulateiMerge(200, 200, 100000), range(1, 200), "iMerge")
"""

"""nPlotter(simulateIncreasingNBMerge(), range(10000, 1010000, 100000), "bMerge")
nPlotter(simulateIncreasingNIterBMerge(), range(10000, 1010000, 100000), "iterBMerge")
nPlotter(simulateIncreasingNIMerge(), range(10000, 1010000, 100000), "iMerge")
nPlotter(simulateIncreasingNNormalMerge(), range(10000, 1010000, 100000), "nMerge")"""

ls = random.sample(range(1, 100001), 100000)
start = time.time()
print(hbMergeSort(ls, 3))
end = time.time()
print(end - start)
