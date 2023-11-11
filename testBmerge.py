from bSort import bSort


def hbMergeSort(ls, k):
    if len(ls) <= k:
        return bSort(ls)
    if len(ls) % k != 0:
        temp = len(ls) - (len(ls) // k)
        if temp % 2 == 0 and k % 2 != 0:
            split = temp // 2
        else:
            split = (temp + k) // 2
    else:
        if len(ls) % 2 == 0 and k % 2 != 0:
            split = len(ls) // 2
        else:
            split = (len(ls) + k) // 2

    ls1 = ls[:split]
    ls2 = ls[split:]
    l = hbMergeSort(ls1, k)
    r = hbMergeSort(ls2, k)
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
        for x in range(ri,len(r)):
            ls[i] = r[x]
            i = i + 1
    elif ri == len(r):
        for x in range(li,len(l)):
            ls[i] = l[x]
            i = i + 1

    return ls




