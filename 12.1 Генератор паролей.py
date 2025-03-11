from random import randint, choice

length = int(input())
for i in range(length):
    print(chr(choice([randint(65, 90),randint(97,122)])), end='')