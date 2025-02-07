
string: int = input().split()
idx: int = 0
list1: list = []
for i in range(len(string)):
    if i == 0: list1.append(list(string[i]))
    elif i > 0 and string[i] == string[i-1]: list1[idx].extend(list(string[i]))
    else:
        list1.append(list(string[i]))
        idx += 1
print(list1)