my_list = []
m = int(input("Enter the number of elements: "))
for i in range(m):
    my_list.append(str(input("Enter the word: ")))
    
a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
     "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
     "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

count = []
new_list = []
for i in my_list:
    c = 0
    for j in i:
        if j in a:
            c += 1
    count.append(c)
    
    
my_dict = dict(zip(my_list, count))
print(my_dict)

n = len(count)
for i in range(n - 1):
    for j in range((i + 1), n):
        if count[j] < count[i]:
            count[i], count[j] = count[j], count[i]
print(count)

n_count = []
for i in count:
    if i not in n_count:
        n_count.append(i)
        
for i in n_count:
    for key, value in my_dict.items():
        if i == value:
            new_list.append(key)
print(new_list)
