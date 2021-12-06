from typing import List


with open("inputs/4.txt") as file:
    data = file.read()

chosen_str, *boards_strs = data.split('\n\n')
chosen_nums = [int(n) for n in chosen_str.split(',')]


class Board():
    size = 5

    def __init__(self, input_string: str) -> None:
        self.grid: List[List[int]] = [[int(n)for n in line.split()]
                                      for line in input_string.splitlines()]
        self.marked = [[False for _ in range(self.size)]
                       for _ in range(self.size)]

    def mark(self, chosen: int) -> bool:
        for row_i, row in enumerate(self.grid):
            if chosen in row:
                self.marked[row_i][row.index(chosen)] = True

    def has_won(self) -> bool:
        return any(all(x) for x in self.marked + [[row[i] for row in self.marked] for i in range(self.size)])

    def score(self, last_value: int) -> int:
        unmarked = [n for r_i, row in enumerate(self.grid) for c_i, n in enumerate(row)
                    if not self.marked[r_i][c_i]]
        return sum(unmarked) * last_value


boards = [Board(s) for s in boards_strs]


def win_bingo() -> int:
    for n in chosen_nums:
        for board in boards:
            board.mark(n)
            if board.has_won():
                return(board.score(n))


print(f"Part 1: {win_bingo()}")


def lose_bingo() -> int:
    for n in chosen_nums:
        for board in boards:
            board.mark(n)
            if all(b.has_won() for b in boards):
                return(board.score(n))


print(f"Part 1: {lose_bingo()}")
