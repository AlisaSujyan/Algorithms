class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    return 0 if val == 0 else (1 if val > 0 else 2)


def convex_hull(points):
    points.sort(key=lambda p: (p.y, p.x))
    p0 = points[0]

    def polar_angle(p):
        return (p.y - p0.y) / (p.x - p0.x) if p.x != p0.x else float('inf')

    points = [p0] + sorted(points[1:], key=lambda p: (polar_angle(p), (p.x - p0.x) ** 2 + (p.y - p0.y) ** 2))

    hull = [points[0], points[1]]
    for p in points[2:]:
        while len(hull) > 1 and orientation(hull[-2], hull[-1], p) != 2:
            hull.pop()
        hull.append(p)

    return hull


n = int(input("Enter the number of points: "))
points = [Point(int(input("X: ")), int(input("Y: ")))for _ in range(n)]

hull = convex_hull(points)

print("Convex Hull:")
for p in hull:
    print(f"({p.x}, {p.y})")
