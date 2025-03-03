def is_sorted(arr):
    if arr == sorted(arr):
        return True
    else:
        return False

def Ternary_Search(arr, f, n, low, high):
    mid1 = int(low + (high - low)/3)
    mid2 = int(low + (high - low) * 2/3)
    while low <= high:
        if f == arr[mid1]:
            return mid1
        elif f == arr[mid2]:
            return mid2
        elif f > arr[mid2]:
            low = mid2 + 1
            return Ternary_Search(arr, f, n, low, high)
        elif f < arr[mid1]:
            high = mid1 - 1
            return Ternary_Search(arr, f, n, low, high)
        else:
            low = mid1 + 1
            high = mid2 - 1
            return Ternary_Search(arr, f, n, low, high)
    return -1


arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    arr.append(int(input(f"Enter the element {i + 1}: ")))
f = int(input("Enter the element for search: "))

low = 0
high = n - 1
m = Ternary_Search(arr, f, n, low, high)
if is_sorted(arr):
    print("Index: ", m)
else:
    print("Array isn't sorted!")
