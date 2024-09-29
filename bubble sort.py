def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[j] < A[i]:
                A[i],A[j] = A[j],A[i]
    return A

n = int(input("Enter the number of elements: "))
my_list = []
for i in range(n):
    my_list.append(float(input(f"Enter the element{i + 1}: ")))

print("Sorted list! ")
print(bubble_sort(my_list))
