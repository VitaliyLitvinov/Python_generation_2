string = input().lower()
cur_word = []
words = set()
for i in string:
    if i.isalpha(): cur_word.append(i)
    elif cur_word: words.add(''.join(cur_word)); cur_word.clear()
if cur_word: words.add(''.join(cur_word))
print(len(words))