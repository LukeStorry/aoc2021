import re
data = open("inputs/13.txt").read()

dots = set((int(x), int(y)) for x, y in re.findall(r"(\d+),(\d+)", data))
folds = [(axis, int(value)) for axis, value in re.findall(r"fold along ([xy])=(\d+)", data)]

for step, (axis, value) in enumerate(folds):
    if axis == "x":
        moved = [(x, y) for x, y in dots if x > value]
        new = ((value - (x-value), y) for x, y in moved)
    if axis == "y":
        moved = [(x, y) for x, y in dots if y > value]
        new = ((x, value - (y-value)) for x, y in moved)

    dots.difference_update(moved)
    dots.update(new)

    if step == 1:
        print(len(dots))

height = max(y for _, y in dots)+1
width = max(x for x, _ in dots)+1
for y in range(height):
    print(''.join('█' if (x, y) in dots else ' ' for x in range(width)))
