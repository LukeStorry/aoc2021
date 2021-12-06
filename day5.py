from collections import Counter
import re
from typing import List, Tuple


line_parser = re.compile('\d+')
class Line():

    def __init__(self, input_string: str) -> None:
        self.x1, self.y1, self.x2, self.y2 = (int(x) for x in line_parser.findall(input_string))

    def __repr__(self) -> str:
        return f"<Line {self.x1},{self.y1} -> {self.x2},{self.y2}"

    def is_straight(self) -> bool:
        return self.x1 == self.x2 or self.y1 == self.y2

    def covers(self) -> List[Tuple[int, int]]:
        if self.x1 == self.x2:
            return ((self.x1, y) for y in range(min(self.y1, self.y2), max(self.y1, self.y2)+1))
        elif self.y1 == self.y2:
            return ((x, self.y1) for x in range(min(self.x1, self.x2), max(self.x1, self.x2)+1))
        else:
            x_step = -1 if self.x1 > self.x2 else 1
            y_step = -1 if self.y1 > self.y2 else 1
            xs = range(self.x1, self.x2+x_step, x_step)
            ys = range(self.y1, self.y2+y_step, y_step)
            return zip(xs, ys)


with open("inputs/5.txt") as file:
    data = file.read()

lines = [Line(s) for s in data.splitlines()]

# Part 1
straight_lines = (line for line in lines if line.is_straight())
straight_line_coverage = [coord for line in straight_lines for coord in line.covers()]
straight_overlaps = sum(1 for count in Counter(straight_line_coverage).values() if count >= 2)
print(f"Part 1: {straight_overlaps}")  # 6283

# Part 2
all_line_coverage = [coord for line in lines for coord in line.covers()]
all_overlaps = sum(1 for count in Counter(all_line_coverage).values() if count >= 2)
print(f"Part 2: {all_overlaps}")  # 18864
