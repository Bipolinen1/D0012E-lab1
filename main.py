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
"""plotter(simulatebMerge(200, 200, 100000), range(1, 200), "bMerge")
plotter(simulateIterBMerge(200, 200, 100000), range(1, 200), "iterBMerge")
plotter(simulateiMerge(200, 200, 100000), range(1, 200), "iMerge")
"""

nPlotter(simulateIncreasingNBMerge(), range(100000, 1100000, 100000), "bMerge")
nPlotter(simulateIncreasingNIterBMerge(), range(100000, 1100000, 100000), "iterBMerge")
nPlotter(simulateIncreasingNIMerge(), range(100000, 1100000, 100000), "iMerge")
nPlotter(simulateIncreasingNNormalMerge(), range(100000, 1100000, 100000), "nMerge")

"""nPlotter(simulateIncreasingNBMerge(), range(10000, 110001, 10000), "bMerge")
nPlotter(simulateIncreasingNBSort(), range(10000, 110001, 10000), "bSort")
nPlotter(simulateIncreasingNIterBSort(), range(10000, 110001, 10000), "iterBSort")
nPlotter(simulateIncreasingNInsertionSort(), range(10000, 50001, 10000), "insertionSort")"""
