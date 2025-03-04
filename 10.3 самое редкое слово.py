list_words: list = [word.rstrip('.,!?:;-') for word in input().lower().split()]
dict_words = {}
for word in list_words:
    dict_words[word] = dict_words.get(word, 0) + 1
min_word = ''
min_value = 999
for key, value in dict_words.items():
    if  value < min_value:
        min_value = value
        min_word = key
    elif  value == min_value and min_word > key:
        min_value = value
        min_word = key
print(min_word)