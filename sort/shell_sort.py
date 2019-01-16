# insert sort, too

def sort(arr) :
    gap = len(arr) // 2
    while gap > 0 :
        for i in range(gap, len(arr)) :
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp :
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap //= 2
    return arr

print(sort([3, 2, 1, 4, 5, 8, 2, 1]))

