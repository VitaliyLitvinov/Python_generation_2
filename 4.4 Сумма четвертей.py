cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
n = int(input())
lst = []
for i in range(n):
    tmp = [int(i) for i in input().split()]
    lst.append(tmp)
for i in range(n):
    for j in range(n):
        if i>j and i<n-1-j: cnt4 += lst[i][j]
        elif i<j and i>n-1-j: cnt2 += lst[i][j]
        elif i<j and i<n-1-j: cnt1 += lst[i][j]
        elif i>j and i>n-1-j: cnt3 += lst[i][j]
print(f'Верхняя четверть: {cnt1}')
print(f'Правая четверть: {cnt2}')
print(f'Нижняя четверть: {cnt3}')
print(f'Левая четверть: {cnt4}')
