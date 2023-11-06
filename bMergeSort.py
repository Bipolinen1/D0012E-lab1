from bSort import bSort
from bSort import binarySearch
import insertionSort


def splitList(ls, chunk_size):
    return [ls[i:i + chunk_size] for i in range(0, len(ls), chunk_size)]


"""def bMergeSort(ls, k):
    length = len(ls)
    newList = []
    ls = splitList(ls, k)
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
    return ls"""


def bMergeSort(ls, k):
    middle = len(ls)//2
    if len(ls) > k:
        left = bMergeSort(ls[:middle], k)
        right = bMergeSort(ls[middle:], k)
        i = 0
        j = 0
        n = 0
        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                ls[n] = left[i]
                i += 1
            else:
                ls[n] = right[j]
                j += 1
            n += 1
        while i < len(left)-1:
            ls[n] = left[i]
            i += 1
            n += 1
        while j < len(right)-1:
            ls[n] = left[j]
            j += 1
            n += 1

    return bSort(ls)



