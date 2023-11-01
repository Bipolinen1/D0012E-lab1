def insertionSort(ls):
    length = len(ls)
    if length <= 1:
        return ls
    for i in range(1, length):
        key = ls[i]
        j = i-1
        while key < ls[j] and j >= 0:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = key
    return ls


"""list1 = [5, 3, 1, 6, 2, 10, -12]
print(insertionSort(list1))"""
