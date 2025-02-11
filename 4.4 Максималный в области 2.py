n = int(input())
lst = []
for i in range(n):
    tmp = [int(i) for i in input().split()]
    lst.append(tmp)
maximum = -99999
for i in range(n):
    for j in range(n):
        if i >= j and i <= n - 1 - j or i <= j and i >= n - 1 - j:
            if lst[i][j] > maximum: maximum = lst[i][j]

print(maximum)