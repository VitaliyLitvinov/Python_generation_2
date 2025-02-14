matrix: int = [input().split() for i in range(int(input()))]
n: int = len(matrix)
for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
for i in range(n):
    print(*matrix[i])
