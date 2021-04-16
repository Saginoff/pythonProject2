a = [[1, 2, 3], [7, 8, 9]]
b = [[4, 5, 6], [10, 11, 12]]
c=[[]]
for i in range(len(a)-1):
    for j in range(len(a[0]) - 1):
        c[i][j] = a[i][j] + b[i][j]

print(c)