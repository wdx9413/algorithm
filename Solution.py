def twoSum(numbers, target):
    result = []
    m = {}
    for i, e in enumerate(numbers):
        remain = target - e
        if remain in m:
            result.append(m[remain])
            result.append(i)
            return result
        m[e] = i
    return result

if __name__ == "__main__":
    numbers = [1, 5 , 4, 2, 1, 8, 6, 5, 11, 24, 15]
    target = 5
    result = twoSum(numbers, target)
    print(result)
