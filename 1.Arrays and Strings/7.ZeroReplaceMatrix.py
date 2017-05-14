mat = [[1,2,3,4],
        [5,6, 7, 8],
        [9, 0, 11, 12],
        [13, 14, 15, 16]]

index = []
for row in xrange(len(mat)):        
    for j in xrange(len(mat)):
        if mat[row][j] == 0:
            index.append([row, j])


for i in index:
    mat[i[0]] = [0]*len(mat)


for [i,j] in index:
    for k in xrange(len(mat)):
        mat[k][j] = 0
print mat
