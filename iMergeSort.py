from insertionSort import insertionSort


def splitList(ls, chunk_size):
    return [ls[i:i + chunk_size] for i in range(0, len(ls), chunk_size)]


def iMergeSort(ls, k):
    length = len(ls)
    newList = []
    ls = splitList(ls, k)
    while len(ls) < length:
        for i in ls:
            insertionSort(i)
        if len(ls) % 2 == 0:
            for i in range(0, len(ls)-1, 2):
                newList += ls[i] + ls[i + 1]
        else:
            newList += ls[len(ls) - 1]
            for i in range(0, len(ls)-1, 2):
                newList += ls[i] + ls[i + 1]
        ls = newList
    insertionSort(ls)
    return ls


