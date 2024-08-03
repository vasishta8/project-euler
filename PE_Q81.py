matrixFile = open("0081_matrix.txt", "r")
matrixLines = matrixFile.readlines()
matrix = []
for x in matrixLines:
    cur = []
    for y in x.split(","):
        cur.append(int(y))
    matrix.append(cur)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i==0 and j==0:
            pass
        elif i==0:
            matrix[i][j] += matrix[i][j-1]
        elif j==0:
            matrix[i][j] += matrix[i-1][j]
        else:
            matrix[i][j] += min([matrix[i-1][j], matrix[i][j-1]])
print(matrix[len(matrix)-1][len(matrix[0])-1])