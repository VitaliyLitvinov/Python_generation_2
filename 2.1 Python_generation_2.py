# На вход программе подается натуральное число.
# Напишите программу, которая вставляет в заданное число запятые
# в соответствии со стандартным американским соглашением о запятых в больших числах.
number = input()[::-1]
k = 0
for i in range(3, len(number), 3):
    if len(number) < 4:
        print(number)
        break
    else:
        number = number[:(i+k)] + ',' + number[i+k:]
    k+=1
print(number[::-1])