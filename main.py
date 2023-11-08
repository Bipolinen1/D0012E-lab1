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
plotter(simulatebMerge(100, 50, 10000), range(1, 100), "bMerge10000")
plotter(simulateIterBMerge(100, 50, 10000), range(1, 100), "iterBMerge10000")
plotter(simulateiMerge(100, 50, 10000), range(1, 100), "iMerge10000")
plotter(simulateNormalMerge(100, 50, 10000), range(1, 100), "normalMerge10000")
