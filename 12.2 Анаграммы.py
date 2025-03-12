from random import shuffle
word = input()
letters = list(word)
shuffle(letters)
print(''.join(letters))