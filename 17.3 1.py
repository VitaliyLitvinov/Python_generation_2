with open("text.txt", encoding="utf8") as text:
    file = text.read().rstrip()
    result = ''.join(reversed(file))
print(result)
