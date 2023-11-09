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
plotter(simulatebMerge(100, 300, 100000), range(1, 100), "bMerge100000,300 iter")
plotter(simulateIterBMerge(100, 300, 100000), range(1, 100), "iterBMerge100000,300 iter")
plotter(simulateiMerge(100, 300, 100000), range(1, 100), "iMerge100000,partSort")
plotter(simulateNormalMerge(100, 300, 100000), range(1, 100), "normalMerge100000,300 iter")
