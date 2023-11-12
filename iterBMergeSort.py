from iterBSort import iterBSort
import math

def iterbMergeSort(ls,k):
    n = len(ls) // k
    if len(ls) <= k:
        return iterBSort(ls)

    k_mid = math.ceil(n/2)

    r = iterbMergeSort(ls[k * k_mid:], k)
    l = iterbMergeSort(ls[:k*k_mid], k)

    i = 0
    li = 0
    ri = 0

    while li < len(l) and ri < len(r):
        if l[li] < r[ri]:
            ls[i] = l[li]
            li = li + 1
        else:
            ls[i] = r[ri]
            ri = ri + 1
        i = i + 1

    if li == len(l):
        for x in range(ri, len(r)):
            ls[i] = r[x]
            i = i + 1
    elif ri == len(r):
        for x in range(li, len(l)):
            ls[i] = l[x]
            i = i + 1
    return ls
