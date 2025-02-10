for _ in range(int(input())):
    lst = list(map(int, input().split()))
    avg = sum(lst) / len(lst)
    print(sum(i > avg for i in lst))