from bMergeSort import *
from iMergeSort import *
from iterBMergeSort import *
import time
import random
from plot import *
from simulatebMerge import *
from simulateIterBMerge import *
from simulateiMerge import *
from simulateNormalMerge import *
from simulateiMerge import *
plotter(simulatebMerge(100, 50, 100000), range(1, 100), "bMerge")
plotter(simulateIterBMerge(100, 50, 100000), range(1, 100), "iterBMerge")
plotter(simulateiMerge(100, 50, 100000), range(1, 100), "iMerge")
plotter(simulateNormalMerge(100, 50, 100000), range(1, 100), "normalMerge")
