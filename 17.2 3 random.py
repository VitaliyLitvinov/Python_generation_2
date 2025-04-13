from random import randrange
file = open('lines.txt', encoding='utf8')
content = file.readlines()
n = randrange(0,len(content))
print(content[n].rstrip())
file.close()