import re
from collections import Counter


data = open("inputs/14_test.txt").read().split('\n\n')
polymer, insertion_rules = data[0], {(f1, f2): t for f1, f2, t in re.findall(r"(.)(.) -> (.)",  data[1])}


class Node:
    def __init__(self, char: str, next) -> None:
        self.char = char
        self.next = next

    def step(self):
        self.next = Node(insertion_rules[self.char, self.next.char], self.next)
        return self.next

    def __repr__(self) -> str:
        return f"{self.char}"


nodes = [Node(c, None) for c in polymer]
for x, y in zip(nodes, nodes[1:]):
    x.next = y


for i in range(40):
    print(i)
    nodes.extend([node.step() for node in nodes if node.next is not None])


c = Counter(n.char for n in nodes).most_common()
print(c[0][1] - c[-1][1])
