import math
def MM(A, B):
    C = [[0, 0],
         [0, 0]]
    C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return(C)
def power(A, B):
    n = len(A)
    m = len(A[0])
    l = len(B)
    k = len(B[0])
    if n == k and l == m and math.log2(n) == int(math.log2(n)) and math.log2(m) == int(math.log2(m)):
                                                return True
def check(A, B):
    return len(A) == len(B) == 2

def add(A, B):
    if not power(A, B):
        m = math.log2(max(len(A), len(A[0])))
        n = math.ceil(m)
        k = pow(2, n)
        A_1 = [[0] * k for _ in range(k)]
        B_1 = [[0] * k for _ in range(k)]
        for i in range(len(A)):
            for j in range(len(A[0])):
                A_1[i][j] = A[i][j]
        for i in range(len(B)):
            for j in range(len(B[0])):
                B_1[i][j] = B[i][j]
        return A_1, B_1
def sum(A, B):
    C = [[0, 0],
         [0, 0]]
    for i in range(2):
        for j in range(2):
            C[i][j] = A[i][j] + B[i][j]
    return C


def unite(A, B, C, D):
    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("D:", D)
    result = []
    for i in range(len(A)):
        result.append(A[i] + B[i])
    for i in range(len(C)):
        result.append(C[i] + D[i])

    return result

    
def divide(new_A, new_B):
    size = len(new_A)  
    mid = size // 2 
    
    A_L1 = [row[:mid] for row in new_A[:mid]]
    A_R1 = [row[mid:] for row in new_A[:mid]]
    A_L2 = [row[:mid] for row in new_A[mid:]]
    A_R2 = [row[mid:] for row in new_A[mid:]]
    
    
    B_L1 = [row[:mid] for row in new_B[:mid]]
    B_R1 = [row[mid:] for row in new_B[:mid]]
    B_L2 = [row[:mid] for row in new_B[mid:]]
    B_R2 = [row[mid:] for row in new_B[mid:]]

    if not check(A_L1, B_L1):
        divide(A_L1, B_L1)
        divide(A_R1, B_L2)
        divide(A_L1, B_R2)
        divide(A_R1, B_R2)

        divide(A_L2, B_L1)
        divide(A_R2, B_L2)
        divide(A_L2, B_R2)
        divide(A_R2, B_R2)
        
    else:
        M = MM(A_L1, B_L1)
        N = MM(A_R1, B_L2)
        
        K = MM(A_L1, B_R1)
        L = MM(A_R1, B_R2)

        D = MM(A_L2, B_L1)
        F = MM(A_R2, B_L2)
        
        G = MM(A_L2, B_R1)
        H = MM(A_R2, B_R2)
        

        return unite(sum(M, N), sum(K, L), sum(D, F), sum(G, H))
    
        
       
    
"""A = [[1, 4, 2],
     [2, 5, 1],
     [2, 5, 1]]

B = [[3, 1, 2],
     [2, 3, 3],
     [2, 5, 1]]"""

A = [[1, 2],
     [2, 1],
     [4, 5],
     [3, 6]]

B = [[3, 3, 2],
     [2, 2, 3]]




new_A, new_B = add(A, B)
print(MM(A, B))
print(check(A, B))
print(power(A, B))
print(add(A, B))
print(divide(new_A, new_B))
F = divide(new_A, new_B)

M = [[0] * len(B[0]) for _ in range(len(A))]
for i in range(len(A)):
    for j in range(len(B[0])):
        M[i][j] = F[i][j]
for row in M:
    print(row)

