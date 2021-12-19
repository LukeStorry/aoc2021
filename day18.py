from __future__ import annotations
from dataclasses import dataclass
from re import findall
from typing import Union


@dataclass
class Pair:
    left: Union[int, Pair]
    right: Union[int, Pair]

    @staticmethod
    def from_string(string: str, i=0) -> Pair:
        if (current_char := string[i]) == '[':
            left, i = Pair.from_string(string, i+1)
            right, i = Pair.from_string(string, i+1)

            if i < len(string)-1:
                return (Pair(left, right), i+1)
            else:
                return Pair(left, right)

        elif current_char.isdigit():
            return int(current_char), i + 1

    def __add__(self, other) -> Pair:
        return Pair(self, other).reduced()

    def reduced(self) -> Pair:

        return self

    def explode(self, depth):
        exploder = self.exploder()
        if exploder is None:
            return False
        start = str()
         # Attempt two, trying to get the string, replace the numbers, and return again.



    def exploder(self, depth=1):
        if depth == 3:

            # if children, then explode them - but how to propogate values - try other child then call to parent, recursively!
            return self

        return (isinstance(self.left, Pair) and self.left.explode(depth+1)) or (isinstance(self.right, Pair) and self.right.explode(depth+1))

    def max_nested(self) -> int:
        left = self.left.max_nested() + 1 if isinstance(self.left, Pair) else 0
        right = self.right.max_nested() + 1 if isinstance(self.right, Pair) else 0
        return max(left, right)

    def __repr__(self) -> str:
        return f"<{self.left}.{self.right}>"


# Pair.from_string("[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]")
# Pair.from_string("[[[[1,2],[3,4]],[[5,6],[7,8]]],9]")
# Pair.from_string("[[[[[9,8],1],2],3],4]").explode()
# Pair.from_string("[[6,[5,[4,[3,2]]]],1]").explode()
Pair.from_string("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]").explode()
