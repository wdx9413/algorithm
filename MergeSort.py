def sort(arr, l, h):
    if l < h :
        mid = (l + h) // 2
        sort(arr, l, mid)
        sort(arr, mid + 1, h)
        merge(arr, l, mid, h)

def merge(arr, l, mid, h):
    a = arr[l : mid + 1]
    b = arr[mid + 1 : h + 1]
    i = 0
    j = 0
    k = l
    while i < len(a) and j < len(b) and k <= h:
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
            k += 1
        else:
            arr[k] = b[j]
            k += 1
            j += 1
    while i < len(a) and k <= h:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b) and k <= h:
        arr[k] = b[j]
        j += 1
        k += 1

arr = [1, 5, 32, 2, 4, 6, 123, 43, 1, 6, 312, 413, 1234, 1]
print(arr)
sort(arr, 0, len(arr) - 1)
print(arr)


