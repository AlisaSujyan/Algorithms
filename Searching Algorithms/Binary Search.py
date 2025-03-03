def is_sorted(arr):
    if arr == sorted(arr):
        return True
    else:
        return False

def Binary_Search(arr, f, n, low, high):
    mid = int(low + (high - low)/2)
    while low <= high:
        if f == arr[mid]:
            return mid
        elif f > arr[mid]:
            low = mid + 1
            return Binary_Search(arr, f, n, low, high)
        elif f < arr[mid]:
            high = mid - 1
            return Binary_Search(arr, f, n, low, high)
    return -1


arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    arr.append(int(input(f"Enter the element {i + 1}: ")))
f = int(input("Enter the element for search: "))

low = 0
high = n - 1
m = Binary_Search(arr, f, n, low, high)
if is_sorted(arr):
    print("Index: ", m)
else:
    print("Array isn't sorted!")
