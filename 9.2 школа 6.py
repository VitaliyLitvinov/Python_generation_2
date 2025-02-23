m = int(input())
students = set()
for _ in range(m):
    tmp = set()
    for _ in range(int(input())):
        tmp.add(input())
    if len(students) == 0: students.update(tmp)
    else: students &= tmp
print(*sorted(students), sep='\n')
