def Naive(T, P):
    n = len(T)
    m = len(P)
    for s in range(n - m + 1):
        if P[0:m] == T[s:(s + m)]:
            return s

T = input()
P = input()
print("Pattern occurs with shift", Naive(T, P))
