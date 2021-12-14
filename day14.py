import re
from collections import Counter


data = open("inputs/14.txt").read().split('\n\n')
polymer, insertion_rules = data[0], {(f1, f2): t for f1, f2, t in re.findall(r"(.)(.) -> (.)",  data[1])}

char_count = Counter(polymer)
pairs_count = Counter(zip(polymer, polymer[1:]))

for i in range(40):
    for pair, count in list(pairs_count.items()):
        new = insertion_rules[pair]
        char_count[new] += count
        pairs_count[pair[0], new] += count
        pairs_count[new, pair[1]] += count
        pairs_count[pair] -= count

    if i == 9:
        print(char_count.most_common()[0][1] - char_count.most_common()[-1][1])

print(char_count.most_common()[0][1] - char_count.most_common()[-1][1])
