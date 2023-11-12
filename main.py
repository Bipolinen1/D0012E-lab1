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
from testBmerge import *
from testBmerge2 import *

"""plotter(simulatebMerge(200, 50, 100000), range(1, 200), "bMerge")
plotter(simulateIterBMerge(200, 50, 100000), range(1, 200), "iterBMerge")
plotter(simulateiMerge(200, 50, 100000), range(1, 200), "iMerge")"""


"""nPlotter(simulateIncreasingNBMerge(), range(10000, 1010000, 100000), "bMerge")
nPlotter(simulateIncreasingNIterBMerge(), range(10000, 1010000, 100000), "iterBMerge")
nPlotter(simulateIncreasingNIMerge(), range(10000, 1010000, 100000), "iMerge")
nPlotter(simulateIncreasingNNormalMerge(), range(10000, 1010000, 100000), "nMerge")"""


nPlotter(simulateIncreasingNBMerge(), range(10000, 200001, 10000), "bMerge")
nPlotter(simulateIncreasingNBSort(), range(10000, 200001, 10000), "bSort")
nPlotter(simulateIncreasingNIterBSort(), range(10000, 200001, 10000), "iterBSort")
nPlotter(simulateIncreasingNISort(), range(10000, 50001, 10000), "insertionSort")


