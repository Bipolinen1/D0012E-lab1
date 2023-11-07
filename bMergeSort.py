from bSort import bSort


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



