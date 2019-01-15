def sort(arr) :
    for i in range(1, len(arr)) :
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(sort([3, 2, 1, 1, 2, 3, 4]))
