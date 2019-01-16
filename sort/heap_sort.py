def buildMaxHeap(arr):
    for j in range(len(arr) // 2, -1, -1):
        heapify(arr, j, len(arr))

def heapify(arr, root, l):
    left = 2 * root + 1
    right = 2 * root + 2
    largest = root
    if left < l and arr[left] > arr[root]:
        largest = left
    if right < l and arr[right] > arr[largest]:
        largest = right
    if largest != root:
        arr[largest], arr[root] = arr[root], arr[largest]
        heapify(arr, largest, l)

def sort(arr):
    buildMaxHeap(arr)
    print(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr

print(sort([1, 5, 4, 2, 1, 8, 2]))
