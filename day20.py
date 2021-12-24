input = open("inputs/20.txt").read().splitlines()
algorithm = [c == '#' for c in input[0]]
lit = {(x, y) for y, row in enumerate(input[2:]) for x, c in enumerate(row) if c == '#'}

for step in range(1, 51):
    (xmin, xmax), (ymin, ymax) = ((min(n), max(n)) for n in zip(*lit))
    lit = {(x, y) for x in range(xmin-1, xmax+2) for y in range(ymin-1, ymax+2)
           if algorithm[int(''.join('1' if (i, j) in lit or ((step-1) % 2 and (xmin > i or xmax < i or ymin > j or ymax < j)) else '0'
                                    for i, j in ((x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1))), 2)]}
    if step == 2:
        print(len(lit))  # 5225
print(len(lit))  # 18131
