characters = 256 

def NextState(ptn, M, S, x):
    if S < M and x == ptn[S]:
        return S + 1
    for n in range(S, 0, -1):
        if ptn[n - 1] == x:
            if ptn[:n - 1] == ptn[S - n + 1:S]:
                return n
    return 0

def compute(ptn, M):
    TF = [{} for _ in range(M + 1)]  
    for S in range(M + 1):
        for char in set(ptn): 
            TF[S][char] = NextState(ptn, M, S, char)
    return TF

def search(ptn, txt):
    M = len(ptn)
    N = len(txt)
    TF = compute(ptn, M)
    S = 0

    for i in range(N):
        char = txt[i]
        S = TF[S].get(char, 0)  
        if S == M:
            print(f"Pattern found at index: {i - M + 1}")


T = input("Enter the text: ")
P = input("Enter the pattern: ")

search(P, T)

