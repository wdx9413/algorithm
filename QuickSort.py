import random
def sort(arr, l, r):
    if l < r:
        index = randomPartition(arr, l, r)
        print(index)
        sort(arr, l, index - 1)
        sort(arr, index + 1, r)

def randomPartition(arr, l, r):
    i = random.randint(l ,r)
    arr[i], arr[l] = arr[l], arr[i]
    return partition(arr, l , r)
    

def partition(arr, l, r):
    key = arr[r]
    i = l
    for j in range(l, r):
        if  arr[j] < key:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


#def partition(arr, l, r):
#    key = arr[l]
#    i = l
#    j = r
#    while i < j:
#        while arr[j] >= key and j > i:
#            j -= 1
#        arr[i] = arr[j]
#        while arr[i] <= key and j > i:
#            i += 1
#        arr[j] = arr[i]
#    arr[i] = key
#    return i;

arr = [1, 4, 2, 5, 2, 8, 5, 12, 4, 15, 14, 13, 11]
print(arr)
sort(arr, 0, len(arr) - 1)
print(arr)
