def iterBinarySearch(ls, value, start, end):
    while start != end:
        middle = (start + end) // 2
        if start > end:
            return start
        elif value < ls[middle]:
            end = middle - 1
        elif value > ls[middle]:
            start = middle + 1
        else:
            return middle
    if ls[start] > value:
        return start
    else:
        return start + 1


def iterBSort(ls):
    length = len(ls)
    for i in range(1, length):
        value = ls[i]
        j = iterBinarySearch(ls, value, 0, i - 1)
        popValue = ls.pop(i)
        ls.insert(j, popValue)
    return ls
