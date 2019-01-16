def quicksort(arr, l, h) :
    if l < h :
        index = partition(arr, l, h)
        quicksort(arr, l, index - 1)
        quicksort(arr, index + 1, h)
    return arr

def partition(arr, l, h) :
    key = arr[h]
    i = l - 1
    for j in range(l, h) :
        if arr[j] < arr[h]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[h] = arr[h], arr[i]
    return i
def sort(arr) :
    return quicksort(arr, 0, len(arr) - 1)
print(sort([1, 3, 2, 4, 5, 2, 10]))
