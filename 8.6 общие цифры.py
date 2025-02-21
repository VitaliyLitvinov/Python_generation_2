n = int(input())
myset = set(list(input()))
for i in range(n-1):
    string = set(list(input()))
    myset.intersection_update(string)
print(*sorted(myset))

