# Дано пятизначное или шестизначное натуральное число.
# Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
num = input()
def revers_5(num):
    num = num[::-1]
    while num[0]=='0':
         num = num[1:]
    return num
def revers_6(num):
    text = num[0] + num[5:0:-1]
    return text
print(revers_5(num) if len(num) == 5 else revers_6(num))