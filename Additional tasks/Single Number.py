def single_number(arr):
    result = 0
    for i in arr:
        result ^= i
    return result

n = int(input("Enter the quantity of numbers: "))
arr = [int(input("Enter the number: "))for _ in range(n)]
result = single_number(arr)
print(result)
