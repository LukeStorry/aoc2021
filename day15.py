from heapq import heappush, heappop
from collections import defaultdict


class PriorityQueue:
    def __init__(self) -> None:
        self.priorities = []
        self.contents = set()

    def pop(self):
        _, next = heappop(self.priorities)
        self.contents.remove(next)
        return next

    def add(self, item, priority):
        self.contents.add(item)
        heappush(self.priorities, (priority, item))

    def not_empty(self) -> bool:
        return len(self.priorities) > 0

    def __contains__(self, item) -> bool:
        return item in self.contents


def cost(risks):
    width, height = max(x for x, _ in risks), max(y for _, y in risks)
    start = (0, 0)
    end = (width, height)

    priority_queue = PriorityQueue()
    priority_queue.add(start, 0)
    costs = defaultdict(lambda:99999)
    costs[start] = 0

    while priority_queue.not_empty():
        x, y = priority_queue.pop()

        if (x, y) == end:
            return costs[end]

        for neighbor in ((i, j) for i, j in ((x-1, y), (x+1, y), (x, y+1), (x, y-1)) if i <= width and i >= 0 and j <= height and j >= 0):
            neighbor_cost = costs[x, y] + risks[neighbor]

            if neighbor_cost < costs[neighbor]:
                costs[neighbor] = neighbor_cost
                if neighbor not in priority_queue:
                    priority_queue.add(neighbor, neighbor_cost - sum(neighbor))


risks = {(x, y): int(n) for y, line in enumerate(open("inputs/15.txt").read().splitlines())for x, n in enumerate(line)}


print(cost(risks))

width, height = max(x for x, _ in risks), max(y for _, y in risks)
larger = {(x + (width+1)*i, y + (height+1)*j): ((n+i+j+8) % 9)+1 for (x, y), n in risks.items() for i in range(5) for j in range(5)}

print(cost(larger))
