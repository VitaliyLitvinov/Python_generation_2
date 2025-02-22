sentence = ''
unique_words = {el.strip(' :,.!?();') for el in sentence.lower().split()}
print(*sorted(unique_words))