class Matrix:
    data = None
    row = 0
    column = 0
    def __init__(self, data):
        self.data = data
        self.row = len(data)
        try:
            self.column = len(data[0])
        except:
            print("data is not a matrix")
    def __str__(self):
        #return "row:%d,column:%d,data:%s"%(self.row, self.column, self.data)
        return "row:{0},column:{1},data:{2}".format(self.row, self.column, self.data)


def matrix_multi(a, b):
    if a.column != b.row:
        print(" a * b error")
        return
    c = [[None] * b.column for i in range(a.row)]
    for i in range(0, a.row):
        for j in range(0, b.column):
            sum = 0
            for k in range(0, b.row):
                sum += a.data[i][k] * b.data[k][j]
            c[i][j] = sum
    return Matrix(c)


if __name__ == "__main__":
    a = Matrix([
        [1, 2, 3],
        [3, 2, 1]
    ])

    b = Matrix([
        [1, 2, 1, 2],
        [2, 3, 2, 3],
        [3, 4, 3, 4]
    ])
    print("a = %s"%a)
    print("b = %s"%b)
    print("a * b = %s"%matrix_multi(a, b))
