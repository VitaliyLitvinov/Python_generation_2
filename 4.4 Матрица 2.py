n = int(input())
m = int(input())
matrix = [[0]*m for _ in range(n)]
for row in range(n):
    for col in range(m):
        word = input()
        matrix[row][col] = word
    print(*matrix[row])
print()
for row in range(m):
    for col in range(n):
        print(matrix[col][row] ,end=' ')
    print()