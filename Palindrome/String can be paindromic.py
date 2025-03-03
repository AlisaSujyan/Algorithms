def Can_be_palindromic(S):
    n = len(S)
    L = []
    for i in S:
        if i not in L:
            L.append(i)
    print(L)
    
    Q = []
    for i in L:
        q = 0
        for j in S:
            if i == j:
                q += 1
        Q.append(q)
    print(Q)

    odd = 0
    for i in Q:
        if i % 2 == 1:
            odd += 1
    print(odd)
    return odd


S = input("Enter the string: ")
odd = Can_be_palindromic(S)
if odd > 1:
    print("String can't be palindromic!")
else:
    print("String can be palindromic!")

    
            
