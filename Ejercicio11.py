a = [[1, 2, 3], [4, 5, 6]]
b = [[-1, 0], [0, 1], [1, 1]]
r = [[0, 0], [0, 0]]


for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            r[i][j] = r[i][j] + a[i][k] * b[k][j]

print(r)