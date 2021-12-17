from re import findall
data = "target area: x=281..311, y=-74..-54"
xmin, xmax, ymin, ymax = (int(v) for v in findall(r"x=([-0-9]+)..([-0-9]+), y=([-0-9]+)..([-0-9]+)", data)[0])


def check(xv, yv):
    x, y, highest = 0, 0, -1
    while y >= ymin and x <= xmax:
        if y <= ymax and x >= xmin:
            return highest
        x += xv
        y += yv
        xv += 0 if xv == 0 else -1 if xv > 0 else 1
        yv -= 1
        highest = max(y, highest)

    return None


successes = [peak
             for xv in range(5, 320)
             for yv in range(-80, 500)
             if (peak := check(xv, yv)) is not None]
print(max(successes))
print(len(successes))
