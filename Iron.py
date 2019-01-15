import math
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
a = [0] * 15
b = [0] * 15
def getP(sum):
    for i in range(1, sum + 1):
        q = -1
        for j in range(1, i + 1):
            t = p[j] + a[i - j]
            if t > q:
                q = t
                b[i] = j
        a[i] = q
    return a[sum]
            

if __name__ == "__main__":
    print(getP(5))
    print(b)
