def is_sorted(arr):
    if arr == sorted(arr):
        return True
    else:
        return False

def Binary_Search(arr, f, low, high):
    if low > high:
        return -1
    mid = int(low + (high - low)/2)
    if f == arr[mid]:
        return mid
    elif f > arr[mid]:
        low = mid + 1
        return Binary_Search(arr, f, low, high)
    elif f < arr[mid]:
        high = mid - 1
        return Binary_Search(arr, f, low, high)

def Exponential_Search(arr, f, i, step):
    while i + step < len(arr):
        if f == arr[i + step]:
            return i + step
        elif f < arr[i + step]:
            return Binary_Search(arr, f, i + 1, i + step - 1)
        elif f > arr[i + step]:
            i = i + step
            step *= 2
    return Binary_Search(arr, f, i + 1, len(arr) - 1)
            


step = 1
arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    arr.append(int(input(f"Enter the element {i + 1}: ")))
f = int(input("Enter the element for search: "))

if is_sorted(arr):
    l = Exponential_Search(arr, f, 0, step)
    if l != -1:
        print("Index: ", l)
    else:
        print("Element not found!")
else:
    print("Array isn't sorted!")

