file_name = input()
file = open(file_name, encoding='utf8')
for line in file:
    print(line.rstrip())
file.close()