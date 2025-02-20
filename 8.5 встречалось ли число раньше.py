numbers = set()
for i in input().split():
    print(['YES', 'NO'][int(i) in numbers])
    numbers.add(int(i))