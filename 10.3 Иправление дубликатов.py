letters: list = input().split()
dict_letters = {}
for i in letters:
    dict_letters[i] = dict_letters.get(i, 0) + 1
    if dict_letters[i] > 1:
        print(f'{i}_{dict_letters[i] - 1}', end=' ')
    else:
        print(i, end=' ')