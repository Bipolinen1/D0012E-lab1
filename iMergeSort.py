from insertionSort import insertionSort


def iMergeSort(ls, k):
    if len(ls) <= k:
        return insertionSort(ls)
    middle = len(ls) // 2
    ls1 = ls[:middle]
    ls2 = ls[middle:]
    l = iMergeSort(ls1, k)
    r = iMergeSort(ls2, k)
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

