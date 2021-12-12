octopods = {(x, y): int(n) for y, line in enumerate(open("inputs/11.txt").read().splitlines())for x, n in enumerate(line)}


def pprint():
    for row in range(10):
        print(''.join(str(n) for ((_, y), n) in octopods.items() if row == y))


total_flashes = 0
for step in range(1, 1000):
    for octopus in octopods.keys():
        octopods[octopus] += 1

    flashed = set()
    while (flash := next((o for (o, n) in octopods.items() if n > 9 and o not in flashed), None)) is not None:
        flashed.add(flash)
        x, y = flash
        for o in ((i, j) for i in range(x-1, x+2) for j in range(y-1, y+2) if i >= 0 and i < 10 and j >= 0 and j < 10):
            octopods[o] += 1

    for flash in flashed:
        octopods[flash] = 0

    total_flashes += len(flashed)

    if step == 100:
        print(f"Part 1: {total_flashes}")

    if len(flashed) == 100:
        print(f"Part 2: {step}")
        break
