set1, set2, set3 = set(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))
print(*sorted(((set1 & set2) - set3), reverse=True))