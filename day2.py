data = "forward 5\n\ndown 5\nforward 8\nup 3\ndown 8\nforward 2\n"

with open("inputs/2.txt") as file:
    data = file.read()

# Part 1
horizontal_position = 0
depth = 0

for command in data.splitlines():
  match command.split():
    case "up", n: depth -= int(n)
    case "down", n: depth += int(n)
    case "forward", n: horizontal_position += int(n)

print(f"Part 1: {horizontal_position * depth}")


# Part 2
horizontal_position = 0
depth = 0
aim = 0

for command in data.splitlines():
  match command.split():
    case "down", n: aim += int(n)
    case "up", n: aim -= int(n)
    case "forward", n: 
        horizontal_position += int(n)
        depth += int(n) * aim

print(f"Part 2: {horizontal_position * depth}")


