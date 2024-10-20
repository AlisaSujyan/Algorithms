def quick_sort(A, l, r):
    if l < r:
        
        q = comp(A, l, r)
        
        quick_sort(A, l, q - 1)
        quick_sort(A, q + 1, r)


def comp(A, l, r):
    
    pivot = A[r]
    i = l - 1 

    for j in range(l, r):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]

   
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


n = int(input("Enter the number of elements: "))
A = []
for i in range(n):
    A.append(int(input(f"Enter the element {i + 1}: ")))

quick_sort(A, 0, len(A) - 1)
print(A)
