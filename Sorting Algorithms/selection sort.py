def selection_sort(A):
    for i in range(len(A) - 1):
        m_index = i
        for j in range((i + 1), len(A)):
            if A[j] < A[m_index]:
                m_index = j
        if m_index != i:
            A[i], A[m_index] = A[m_index], A[i]
    return A

n = int(input("Enter the number of elements: "))
my_list = []
for i in range(n):
    my_list.append(float(input(f"Enter the element {i + 1}: ")))

print("Sorted list! ")
print(selection_sort(my_list))
