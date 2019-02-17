def transpose(A):
    matrix = []
    if (len(A) > 0):
        for x in range(len(A[0])):
            row = []
            for y in range(len(A)):
                row.append(A[y][x])
            matrix.append(row)
            
    return matrix
