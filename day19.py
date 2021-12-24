from collections import Counter


def negativise(coords: list[tuple[int, int, int]]):
    return [
        [(x, y, z) for x, y, z in coords],
        [(-x, y, z) for x, y, z in coords],
        [(x, -y, z) for x, y, z in coords],
        [(x, y, -z) for x, y, z in coords],
        [(-x, -y, z) for x, y, z in coords],
        [(-x, y, -z) for x, y, z in coords],
        [(x, -y, -z) for x, y, z in coords],
        [(-x, -y, -z) for x, y, z in coords]
    ]


def flip(coords: list[tuple[int, int, int]]):
    return [
        [[x, y, z] for x, y, z in coords],
        [[x, z, y] for x, y, z in coords],
        [[y, x, z] for x, y, z in coords],
        [[z, y, x] for x, y, z in coords],
        [[y, z, x] for x, y, z in coords],
        [[z, x, y] for x, y, z in coords]
    ]


class Scanner:
    def __init__(self, n, beacons) -> None:
        self.n = n
        self.beacons = beacons
        self.all_oriented_beacons = [c for f in flip(beacons) for c in negativise(f)]
        self.coordinates = None

    def __repr__(self) -> str:
        return f"<Scanner {self.n} at {self.coordinates}>"

    def find_position(self, aligned_scanners: list):
        for other_scanner in aligned_scanners:
            for oriented_beacons in self.all_oriented_beacons:
                (dx, dy, dz), best_diff = Counter((x-ox, y-oy, z-oz) for x, y, z in oriented_beacons
                                                  for ox, oy, oz in other_scanner.beacons
                                                  ).most_common()[0]
                if best_diff >= 12:
                    self.coordinates = (-dx, -dy, -dz)
                    self.beacons = [(x-dx, y-dy, z-dz) for x, y, z in oriented_beacons]
                    return


scanners: list[Scanner] = []
for line in open("inputs/19.txt").read().splitlines():
    if "scanner" in line:
        id = int(line[12:14])
        beacons = []
    elif line:
        beacons.append(tuple(int(n) for n in line.split(',')))
    else:
        scanners.append(Scanner(id, beacons))

scanners[0].coordinates = (0, 0, 0)

while not all(s.coordinates for s in scanners):
    for scanner in scanners:
        if not scanner.coordinates:
            scanner.find_position(s for s in scanners if s.coordinates)

print(len(set(b for s in scanners for b in s.beacons)))
print(max(sum(abs(a-b) for a, b in zip(s1.coordinates, s2.coordinates)) for s1 in scanners for s2 in scanners))
