def matrix_multiply(A, B):
    n = len(A)
    m = len(B[0])
    result = [ [0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def input_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix

n = int(input("Enter the size of rows in A matrix: "))
m = int(input("Enter the size of rows in B matrix: "))

    
A = input_matrix(n)
B = input_matrix(m)

C = matrix_multiply(A, B)
for row in C:
    print(row)
