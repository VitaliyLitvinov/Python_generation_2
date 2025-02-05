n = int(input())
num = [int(input()) for i in range(n)]
num_prod = []
for i in range(0,len(num)):
    if len(num) < 2:
        num_prod.append(i)
        break
    for k in range(i+1,len(num)):
        num_prod.append(num[i]*num[k])
product = int(input())
print('ДА' if product in num_prod else 'НЕТ')
