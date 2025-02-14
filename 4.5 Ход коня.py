matrix = [['.']*8 for i in range(8)]
xy = input()
x = '87654321'.index(xy[1])
y = 'abcdefgh'.index(xy[0])
print()
matrix[x][y] = 'N'
if 0<=x+1<8 and 0<=y+2<8: matrix[x+1][y+2] = '*'
if 0<=x+2<8 and 0<=y+1<8: matrix[x+2][y+1] = '*'
if 0<=x+1<8 and 0<=y-2<8: matrix[x+1][y-2] = '*'
if 0<=x+2<8 and 0<=y-1<8: matrix[x+2][y-1] = '*'

if 0<=x-1<8 and 0<=y+2<8: matrix[x-1][y+2] = '*'
if 0<=x-2<8 and 0<=y+1<8: matrix[x-2][y+1] = '*'
if 0<=x-1<8 and 0<=y-2<8: matrix[x-1][y-2] = '*'
if 0<=x-2<8 and 0<=y-1<8: matrix[x-2][y-1] = '*'

for i in range(8):
    print(*matrix[i])