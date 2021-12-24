algorithm, _, *input_image = open("inputs/20.txt").read().splitlines()

algorithm = [c == '#' for c in algorithm]

lit = {(x, y) for y, row in enumerate(input_image) for x, c in enumerate(row) if c == '#'}

for step in range(2):
    (xmin, xmax), (ymin, ymax) = ((min(n), max(n)) for n in zip(*lit))

    lit = {(x, y) for x in range(xmin-5, xmax+5) for y in range(ymin-5, ymax+5)
           if algorithm[int(''.join('1' if (i, j) in lit else '0'
                                    for i, j in ((x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1))), 2)]}

print(len(lit))  # 5225
