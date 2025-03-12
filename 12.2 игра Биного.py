from random import randrange
bingo = [[99] * 5 for _ in range(5)]
bingo[2][2] = 0
digits = []
for i in range(5):
    for j in range(5):
        if bingo[i][j] > 0:
            digit = randrange(1, 76)
            while digit in digits:
                digit = randrange(1, 76)
            if digit not in digits :
                bingo[i][j] = digit
                digits.append(digit)
        print(str(bingo[i][j]).ljust(3), end='')
    print()
