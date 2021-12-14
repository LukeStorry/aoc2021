import re
from collections import Counter
data = open("inputs/14.txt").read().split('\n\n')
polymer, insertion_rules = data[0], {(f1, f2): t for f1, f2, t in re.findall(r"(.)(.) -> (.)",  data[1])}

for step in range(10):
    polymer = polymer[0] + ''.join(insertion_rules[a,b]+ b for (a,b) in zip(polymer, polymer[1:]))

c = Counter(polymer).most_common()
print(c[0][1] - c[-1][1])