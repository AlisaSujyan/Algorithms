def Palindrome(T):
    n = len(T)
    for i in range(int(n/2)):
        if T[i] != T[n - i - 1]:
            return False
    return True

def Longest_PS(S):
    m = len(S)
    max_length = 0
    for k in range(m, 1, -1):
        for i in range(m - k + 1):
            substring = S[i : i + k]
            a = Palindrome(substring)

            if a is True:
                max_length = k
                return i, k

S = input("Enter the string: ")
s, l = Longest_PS(S)
print("Palindrome starts at index: ", s)
print("Longest palindromne length is: ", l)
