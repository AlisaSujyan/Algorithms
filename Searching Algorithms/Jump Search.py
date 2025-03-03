import math

def is_sorted(arr):
    if arr == sorted(arr):
        return True
    else:
        return False

def Jump_search(arr, f, n):
    j = int(math.sqrt(n))
    p = 0
    c = 0
    while c <= n - 1:
        if f <= arr[c]:
            return c
        c = c + j
    return c

arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    arr.append(int(input(f"Enter the element {i + 1}: ")))
f = int(input("Enter the element for search: "))
C = Jump_search(arr, f, n)
j = int(math.sqrt(n))
if is_sorted(arr):
    if C > n - 1:
        for i in range(n - 1, n - j - 1, -1):
            if f == arr[i]:
                print("Index: ", i)
                break
    elif C != n - 1:
        for i in range(C, C - j, -1):
            if f == arr[i]:
                print("Index: ", i)
else:
    print("Array isn't sorted!")


