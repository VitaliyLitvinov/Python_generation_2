n = int(input())
maximum = -10000
for i in range(n):
    nums = [int(i) for i in input().split()]
    for j in range(i + 1):
        if nums[j] > maximum: maximum = nums[j]
print(maximum)
