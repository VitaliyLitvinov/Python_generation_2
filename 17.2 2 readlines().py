file_name = input()
file = open(file_name, encoding='utf8')
content = file.readlines()
print(content[-2].rstrip())
file.close()