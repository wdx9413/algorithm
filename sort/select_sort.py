def sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr
print(sort([1, 5, 3, 8, 2, 1, 5, 2, 3]))

