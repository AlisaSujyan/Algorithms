def failureFunction(P):
    m = len(P)
    F = []
    for i in range(m):
        F.append(0)
    F[0] = 0
    j = 1
    l = 0
    while j < m:
        if P[j] == P[l]:
            l = l + 1
            F[j] = l
            j = j + 1
        elif l > 0:
            l = F[l - 1]
        else:
            F[j] = 0
            j = j + 1
    return F

            
def KMPMatch(T, P):
    F = failureFunction(P)
    n = len(T)
    k = len(P)
    i = 0
    j = 0
    M = []
    while i < n:
        if T[i] == P[j]:
            i = i + 1
            j = j + 1
            if j == k:
                M.append(i - j)
                j = F[j - 1]
        else:
            if j != 0:
                j = F[j - 1]
            else:
                i = i + 1
    return M



    
T = input("Enter the text: ")
P = input("Enter the pattern: ")

m = KMPMatch(T, P)
for i in range(len(m)):
    print(f"Pattern{i + 1}: ", m[i])
