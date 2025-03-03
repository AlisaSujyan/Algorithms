def Interpolation_Search(arr, f, low, high):
    pos = int(low + (((f - arr[low]) * (high - low)) / (arr[high] - arr[low])))
    while low <= high:
        if f == arr[pos]:
            return pos
        elif f < arr[pos]:
            high = pos - 1
            return Interpolation_Search(arr, f, low, high)
        elif f > arr[pos]:
            low = pos + 1
            return Interpolation_Search(arr, f, low, high)
    return -1


arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    arr.append(int(input(f"Enter the element(uniformly) {i + 1}: ")))
f = int(input("Enter the element for search: "))

low = 0
high = n - 1
m = Interpolation_Search(arr, f, low, high)
if m != -1:
    print("Index: ", m)
else:
    print("Array isn't sorted!")
