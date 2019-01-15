def mergesort(arr, l, h):
    if l < h:
        mid = (l + h) // 2
        mergesort(arr, l, mid)
        mergesort(arr, mid + 1, h)
        merge(arr, l, mid, h)
    return arr
def merge(arr, l, mid, h):
    a = arr[l: mid + 1]
    b = arr[mid + 1: h + 1]
    i = 0
    j = 0
    k = l
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1

def sort(arr):
    return mergesort(arr, 0, len(arr) - 1)

print(sort([1, 4, 2, 5, 6, 2, 6, 2]))
