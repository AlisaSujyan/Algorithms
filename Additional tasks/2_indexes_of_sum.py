def Value(arr, target):
    for i in range(n - 1):
        current = target - arr[i]
        for j in range(i + 1, n):
            if arr[j] == current:
                return i, j
    i = 0
    j = 0
    return i, j

n = int(input("Enter the size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter the element {i + 1}: ")))

target = int(input("Enter the target: "))
i, j = Value(arr, target)
if i == 0 and j == 0:
    print("Not found")
else:
    print(i, j)
