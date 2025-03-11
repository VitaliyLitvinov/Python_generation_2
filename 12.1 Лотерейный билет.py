from random import randint
numbers = set()
while len(numbers) < 7:
    numbers.add(randint(1, 47))
print(*sorted(numbers), sep=' ')