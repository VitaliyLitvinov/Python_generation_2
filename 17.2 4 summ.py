file = open('numbers.txt', encoding='utf8')
summ = 0
nums = file.readlines()
for line in nums:
    summ += int(line)
print(summ)
file.close()