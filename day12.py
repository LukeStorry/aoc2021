import re
connection_list = re.findall(r"(.+)-(.+)", open("inputs/12.txt").read())

connections = {cave: [[other for other in connection if cave != other][0] for connection in connection_list if cave in connection]
               for cave in set(cave for connection in connection_list for cave in connection)}

complete_trails = []
allowed_small_revisits = False


def findPaths(trail):
    current = trail[-1]

    if current == "end":
        complete_trails.append(trail)
        return

    if current not in connections:
        return

    for next_cave in connections[current]:
        if next_cave == "start":
            continue
        if next_cave.islower():
            already_visited = trail.count(next_cave) > 0
            if not allowed_small_revisits and already_visited:
                continue
            if already_visited and any(c for c in trail if c.islower() and trail.count(c) > 1):
                continue

        findPaths(trail+[next_cave])


findPaths(['start'])
print(len(complete_trails))

complete_trails = []
allowed_small_revisits = True
findPaths(['start'])
print(len(complete_trails))