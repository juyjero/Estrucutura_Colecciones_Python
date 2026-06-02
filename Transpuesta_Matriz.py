A = [[1, 2, 3],
     [4, 5, 6]]
T = []
for j in range(len(A[0])):
    fila = []
    for i in range(len(A)):
        fila.append(A[i][j])
    T.append(fila)
print(T)