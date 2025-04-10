def index(arr, target):
    for i in range(len(arr)):
        my_dict = {index: target - value for index, value in enumerate(arr)}
    my_list = []
    key_for_value = {value: key for key, value in my_dict.items()}
    for i in range(len(arr)):
        if arr[i] in my_dict.values() and i != key_for_value[arr[i]]:
            my_list.append(i)
    print(my_list)

n = int(input("Enter the size of array: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter the element{i+1}: ")))
target = int(input("Enter the target: "))

index(arr, target)
