data = "3,4,3,1,2"

with open("inputs/6.txt") as file:
    data = file.read()


# Part 1
fish = [int(x) for x in data.split(',')]
for _ in range(80):
    fish = [f-1 if f > 0 else 6 for f in fish] + [8 for f in fish if f == 0]
print(f"Part 1: {len(fish)}")  # 359999

# Part 2
fish_list = [int(x) for x in data.split(',')]
fish = {x: fish_list.count(x) for x in range(9)}
for _ in range(256):
    fish = {f-1: c for f, c in fish.items()}
    fish[8] = fish[-1]
    fish[6] = fish.get(6, 0) + fish[-1]
    del fish[-1]
print(f"Part 1: {sum(fish.values())}") # 1631647919273
