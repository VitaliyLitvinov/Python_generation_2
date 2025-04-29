with open("text.txt", encoding="utf8") as data:
    lines = data.readlines()
    for line in lines[::-1]:
        print(line.rstrip())
