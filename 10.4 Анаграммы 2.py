string1 = ''.join(i for i in input() if i not in '.,!?:;- ').lower()
string2 = ''.join(i for i in input() if i not in '.,!?:;- ').lower()
letters1, letters2 = {}, {}
for i in string1:
    letters1[i] = letters1.get(i, 0) + 1
for i in string2:
    letters2[i] = letters2.get(i, 0) + 1
print('YES' if letters1 == letters2 else "NO"