n, m = int(input()), int(input())
maximum = -99999
maxrow = -1
maxcol = -1
matrix  = [[0]*m] * n
for row in range(n):
    lst = [int(i) for i in input().split()]
    matrix[row] = lst
for row in range(n):
    for col in range(m):
        if matrix[row][col] > maximum:
            maximum = matrix[row][col]
            maxrow = row
            maxcol = col
print(maxrow, maxcol)
