import sys
def matrix_chain_order(matrixs):
    matrix_num = len(matrixs) - 1
    m = [[0] * matrix_num for i in range(matrix_num)]
    s = [[0] * matrix_num for i in range(matrix_num)]
      
    for l in range(2, matrix_num + 1):
        for i in range(0, matrix_num - l + 1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + matrixs[i] * matrixs[k+1] * matrixs[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k


    return [m, s]

[m, s] = matrix_chain_order([30, 35, 15, 5, 10, 20, 25])
print(m)
def print_opt(s, i, j):
    str = ""
    if i == j:
        return "A{0}".format(i)
    else:
        str += "("
        str += print_opt(s, i, s[i][j])
        str += print_opt(s, s[i][j] + 1, j)
        str += ")"
        return str
print(s)
print(print_opt(s, 0, 5))
