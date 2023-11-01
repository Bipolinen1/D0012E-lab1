from insertionSort import insertionSort


def splitList(ls, chunkSize):
    return [ls[i:i + chunkSize] for i in range(0, len(ls), chunkSize)]


def iMergeSort(ls, k):
    length = len(ls)
    chunks = len(ls)//k
    chunkSize = len(ls)//chunks
    newList = []
    ls = splitList(ls, chunkSize)
    while len(ls) < length:
        for i in ls:
            insertionSort(i)
        for i in range(0, len(ls)-1, 2):
            newList += ls[i] + ls[i + 1]
        ls = newList
    insertionSort(ls)
    return ls


list1 = [3, 2, 5, 1, 6, 3, 1, 4]
print(iMergeSort(list1, 2))
