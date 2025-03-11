from random import shuffle
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
def shuffle_matrix():
    for i in range(len(matrix)):
        shuffle(matrix[i])
    return matrix

print(shuffle_matrix())