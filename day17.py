from re import findall
data = "target area: x=281..311, y=-74..-54"
# data = "target area: x=20..30, y=-10..-5"
xmin, xmax, ymin, ymax = (int(v) for v in findall(r"x=([-0-9]+)..([-0-9]+), y=([-0-9]+)..([-0-9]+)", data)[0])


def check(xv, yv):
    x, y, highest = 0, 0, -1
    while y > ymax:
        x += xv
        y += yv
        xv += -1 if xv > 0 else 1
        yv -= 1
        highest = max(y, highest)

    if y >= ymin and xmax >= x >= xmin:
        return highest
    return False

best = 0
for xv in range(-50,200):
    for yv in range(-1,200):
        best = max(check(xv,yv), best)


print(best)