n = int(input())
four1, four2, four3, four4 = 0, 0, 0, 0
for i in range(n):
    string = input().split()
    xy = [int(i) for i in string]
    if '0' in xy:
        continue
    else:
        if xy[0] > 0 and xy[1] > 0:
            four1 += 1
        elif xy[0] < 0 and xy[1] > 0:
            four2 += 1
        elif xy[0] < 0 and xy[1] < 0:
            four3 += 1
        elif xy[0] > 0 and xy[1] < 0:
            four4 += 1

print(f'Первая четверть: {four1}')
print(f'Вторая четверть: {four2}')
print(f'Третья четверть: {four3}')
print(f'Четвертая четверть: {four4}')