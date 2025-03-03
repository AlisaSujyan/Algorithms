def Longest_Prefix(arr, n, m):
    q = 0
    for j in range(m-1, -1, -1):
        s = 0
        for i in range(1, n):
            if arr[s][0:j] != arr[i][0:j]:
                break
            else:
                return j
            
            


arr = ["aaasklk", "aaasbdvjh", "aaaskjhdh", "aaaskbfg"]
n = len(arr)
L = []
for i in arr:
    L.append(len(i))
m = min(L)
print(m)
f = Longest_Prefix(arr, n, m)
print(arr[0][0:f])
print(f)
