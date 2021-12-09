from math import prod

heightmap = [[int(n) for n in line] for line in open("inputs/9.txt").read().splitlines()]
width, height = len(heightmap[0]), len(heightmap)


def neighbors(x, y):
    if x != 0:
        yield (x-1, y)
    if y != 0:
        yield (x, y-1)
    if x+1 < width:
        yield (x+1, y)
    if y+1 < height:
        yield (x, y+1)


low_points = [(n, x, y) for y, row in enumerate(heightmap) for x, n in enumerate(row)
              if all(n < heightmap[j][i] for (i, j) in neighbors(x, y))]

# Part 1: Print cost of all low points
print(sum(n+1 for n, *_ in low_points))

# Part 2
# Initialise visited coordinate set with bounding high points
visited = set((x, y) for y in range(height) for x in range(width) if heightmap[y][x] == 9)


def walk_uphill(x, y):
    """Recursively count all non-visited locations reachable"""
    visited.add((x, y))
    return 1 + sum(walk_uphill(i, j) for i, j in neighbors(x, y) if (i, j) not in visited)


# Print product of highest three walks
print(prod(sorted(walk_uphill(x, y) for _, x, y in low_points)[-3:]))
