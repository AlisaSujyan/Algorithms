def Table(P):
    n = len(P)
    M = []
    for i in P:
        if i not in M:
            M.append(i)
    L = [0 for _ in range(len(M))]
    for i in range(n-1):
        if P[i] in M:
            L[M.index(P[i])] = n - i - 1
        L[M.index(P[n-1])] = n
    return M, L


def Same(T, P, i):
    n = len(P)
    for j in range(n):
        if T[i - j] != P[n - 1 - j]:
            return False
    return True
    
        
def BoyerMoore(T, P):
    M, L = Table(P)
    print(Table(P))
    n = len(P)
    i = n - 1
    while i < len(T):
        if Same(T, P, i):
            print(f"Index is: {i - n + 1} ")
            i += n
        else:
            if T[i] in M:
                i += L[M.index(T[i])]
            else :
                i += n
    return "End"
            
 
T = input("Enter the text: ")

P = input("Enter the pattern: ")

print(BoyerMoore(T, P))
