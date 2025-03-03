arr = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
n = len(arr)

print('Original array: ')
print(arr)

for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j>=0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    print(arr)

print('Sorted array: ')    
print(arr)






