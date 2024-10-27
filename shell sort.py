def ShellSort(A):
    n = len(A)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j = j - gap
            A[j] = temp
        gap = gap//2


A = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    A.append(int(input(f"Enter the element{i + 1}: ")))
    
ShellSort(A)
print(A)
