list1: list = input().split()
result = []
n: int = int(input())
for i in range(0,len(list1),n):
    result.append(list(list1[i:i+n]))
print(result)