with open("text.txt", encoding="utf8") as text:
    print(text.read().rstrip()[::-1])
