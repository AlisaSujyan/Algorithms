def Hanoi(N, start, end):
    if N == 1:
        print(start,"->", end)
    else:
        a = 6 - (start + end)  
        Hanoi(N - 1, start, a)  
        print(start,"->", end)
        Hanoi(N - 1, a, end)    

Hanoi(int(input("N: ")), int(input("Start: ")), int(input("End: ")))
