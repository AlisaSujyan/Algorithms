def Orientation(A, B, C):
    a = (B[1] - A[1]) * (C[0] - B[0])
    b = (C[1] - B[1]) * (B[0] - A[0])
    if a - b > 0:
        print("Clockwise", a - b)
        return 1
    elif a - b < 0:
        print("Counterclockwise", a - b)
        return -1
    else:
        print("Collinear")
        return 0

P1 = [int(input("Enter P1")) for _ in range(2)]
Q1 = [int(input("Enter Q1")) for _ in range(2)]
P2 = [int(input("Enter P2")) for _ in range(2)]
Q2 = [int(input("Enter Q2")) for _ in range(2)]


m = Orientation(P1, Q1, P2)
n = Orientation(P1, Q1, Q2)
l = Orientation(P2, Q2, P1)
k = Orientation(P2, Q2, Q1)

if m != n and l != k:
    print("True")
elif m == n == l == k == 0:
    if min(P1, Q1) <= P2 <= max(P1, Q1) or min(P1, Q1) <= Q2 <= max(P1, Q1) or min(P2, Q2) <= P1 <= max(P2, Q2) or min(P2, Q2) <= Q1 <= max(P2, Q2):
        print("Are collinear, intersect")
    else:
        print("Are collinear, do not intersect")
else:
     print("False")
