n, m = int(input()), int(input())
students = {input() for _ in range(n+m)}
if len(students) == n+m: print(m+n)
elif (n+m) - (((n+m) - len(students)) * 2) == 0: print('NO')
else: print((n+m) - (((n+m) - len(students)) * 2))