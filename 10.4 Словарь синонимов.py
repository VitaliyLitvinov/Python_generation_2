words: dict = {}
for _ in range(int(input())):
    key, value = input().split()
    words[key] = value
word: str = input()
if word in words.keys():
    print(words[word])
else:
    for key, value in words.items():
        if value == word: print(key)