from __future__ import annotations
from typing import Optional, Union
from math import floor, ceil


class Pair:
    @staticmethod
    def from_string(string: str, i=0, grand_parent=None) -> Pair:
        if (current_char := string[i]) == '[':
            parent = Pair(grand_parent, None, None)
            parent.left, i = Pair.from_string(string, i+1, parent)
            parent.right, i = Pair.from_string(string, i+1, parent)
            return (parent, i+1) if i < len(string)-1 else parent

        elif current_char.isdigit():
            return int(current_char), i + 1

    def __init__(self, parent: Optional[Pair], left: Union[int, Pair], right: Union[int, Pair]) -> None:
        self.parent = parent
        self.left = left
        self.right = right

    def __add__(self, other) -> Pair:
        new = Pair(None, self, other)
        self.parent = new
        other.parent = new
        return new.reduced()

    def reduced(self) -> Pair:
        while self.explode() or self.split():
            pass
        return self

    def split(self):
        if isinstance(self.left, int) and self.left >= 10:
            self.left = Pair(self, floor(self.left/2), ceil(self.left/2))
            return True
        if isinstance(self.right, int) and self.right >= 10:
            self.right = Pair(self, floor(self.right/2), ceil(self.right/2))
            return True

        return (isinstance(self.left, Pair) and self.left.split()) or (isinstance(self.right, Pair) and self.right.split())

    def explode(self, depth=0):
        if depth == 4:
            self.parent.explode_left(self.left, self)
            self.parent.explode_right(self.right, self)
            if self == self.parent.left:
                self.parent.left = 0
            else:
                self.parent.right = 0
            return True
        return (isinstance(self.left, Pair) and self.left.explode(depth+1)) or (isinstance(self.right, Pair) and self.right.explode(depth+1))

    def explode_left(self, n, previous):
        if previous == self.left:
            if self.parent is not None:
                self.parent.explode_left(n, self)
        else:
            self.add_left(n, go_right=True)

    def explode_right(self, n, previous):
        if previous == self.right:
            if self.parent is not None:
                self.parent.explode_right(n, self)
        else:
            self.add_right(n, go_left=True)

    def add_left(self, n, go_right=False):
        if isinstance(self.left, Pair):
            if go_right:
                self.left.add_right(n)
            else:
                self.left.add_left(n)
        else:
            self.left += n

    def add_right(self, n, go_left=False):
        if isinstance(self.right, Pair):
            if go_left:
                self.right.add_left(n)
            else:
                self.right.add_right(n)
        else:
            self.right += n

    def __str__(self) -> str:
        return f"[{self.left},{self.right}]"

    def magnitude(self) -> int:
        mag_left = self.left.magnitude() if isinstance(self.left, Pair) else self.left
        mag_right = self.right.magnitude() if isinstance(self.right, Pair) else self.right
        return 3 * mag_left + 2*mag_right


# pairs = list(map(Pair.from_string, open("inputs/18.txt").read().splitlines()))
# result = sum(pairs[1:], start=pairs[0])
# print(result)
# print(result.magnitude())

# All good for first 4 sums, then this? one fails.
print(Pair.from_string("[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]") +
      Pair.from_string("[7,[5,[[3,8],[1,4]]]]"))
      
# # Should be:
print("[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]")
