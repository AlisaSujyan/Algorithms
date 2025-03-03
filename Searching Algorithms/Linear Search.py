def Linear_Search(arr, f):
    for i in range(len(arr)):
        if arr[i] == f:
            return i


arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    arr.append(int(input(f"Enter the element {i + 1}: ")))
f = int(input("Enter the element for search: "))

index = Linear_Search(arr, f)
if index == None:
    print("Element isn't found!")
else:
    print("Index is: ", index)
