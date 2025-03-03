class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def Left_index(points):
    minn = 0
    for i in range(1, len(points)):
        if points[i].x < points[minn].x or (points[i].x == points[minn].x and points[i].y > points[minn].y):
            minn = i
    return minn

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    if val > 0:
        return 1
    else:
        return 2

def convexHull(points, n):

    l = Left_index(points)
    hull = []

    p = l
    while True:
        hull.append(p)
        q = (p + 1) % n

        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q
        if p == l:
            break

    for i in hull:
        print(points[i].x, points[i].y)


n = int(input("Enter the number of points: "))
points = [Point(int(input("X: ")), int(input("Y: ")))for _ in range(n)]

convexHull(points, len(points))
