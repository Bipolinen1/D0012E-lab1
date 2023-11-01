from bSort import bSort
from bSort import binarySearch
import insertionSort


def splitList(ls, chunkSize):
    return [ls[i:i + chunkSize] for i in range(0, len(ls), chunkSize)]


def bMergeSort(ls, k):
    length = len(ls)
    chunks = len(ls)//k
    chunkSize = len(ls)//chunks
    newList = []
    ls = splitList(ls, chunkSize)
    while len(ls) < length:
        for i in ls:
            bSort(i)
        if len(ls) % 2 == 0:
            for i in range(0, len(ls)-1, 2):
                newList += ls[i] + ls[i + 1]
        else:
            for i in range(0, len(ls)-1, 2):
                newList += ls[i] + ls[i + 1]
            newList += ls[len(ls) - 1]
        ls = newList
    bSort(ls)
    return ls



