file = open('prices.txt', encoding='utf8')
content = file.read().split()
summ = 0
for i in range(2,len(content),3):
    summ += int(content[i - 1]) * int(content[i])
print(summ)

file.close()