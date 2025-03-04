word1, word2 = input().lower(), input().lower()
letters1, letters2 = {}, {}
for i in word1:
    letters1[i] = letters1.get(i, 0) + 1
for i in word2:
    letters2[i] = letters2.get(i, 0) + 1
print('YES' if letters1 == letters2 else "NO")
