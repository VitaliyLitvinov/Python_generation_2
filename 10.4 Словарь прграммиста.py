n = int(input())
slang_dict = {}
for _ in range(n):
    s = input().split(':')
    slang_dict[s[0].lower()] = s[1].lstrip()
m = int(input())
for _ in range(m):
    s = input().lower()
    ans = slang_dict.get(s, 'Не найдено')
    print(ans)