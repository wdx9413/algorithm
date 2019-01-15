import math

def sort(arr):
    heapSize = len(arr)
    buildMaxHeap(arr, heapSize)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapSize -= 1
        maxHeapify(arr, 0, heapSize)

def buildMaxHeap(arr, heapSize):
    for i in range(math.floor(len(arr) / 2) - 1, -1, -1):
        maxHeapify(arr, i, heapSize)

def maxHeapify(arr, i, heapSize):
    l = left(i)
    r = right(i)
    largest = i
    if l < heapSize and arr[l] > arr[i]:
        largest = l
    if r < heapSize and arr[r] > arr[largest]:
        largest = r
    if largest != i :
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest, heapSize)

def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2
def parent(i):
    return math.floor(i / 2) - 1

arr = [1, 3, 5, 6, 1, 2, 3, 5, 4, 8]
print(arr)
sort(arr)
print(arr)
