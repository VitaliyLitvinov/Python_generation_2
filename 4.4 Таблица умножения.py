n, m, = int(input()), int(input())
for row in range(n):
    lst = []
    for col in range(m):
        lst.append(row * col)
    print(*lst)