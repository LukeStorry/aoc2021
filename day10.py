subsystem = open("inputs/10.txt").read().splitlines()

chunks = ('()', '[]', '{}', '<>')
syntax_error_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
completion_points = {'(': 1, '[': 2, '{': 3, '<': 4}

total_syntax_error_score = 0
completion_scores = []
for line in subsystem:
    while any(chunk in line for chunk in chunks):
        for chunk in chunks:
            line = line.replace(chunk, '')

    first_illegal = next((c for c in line if c in ')]}>'), False)

    if first_illegal:  # Part 1
        total_syntax_error_score += syntax_error_points[first_illegal]
    else:  # Part 2
        completion_scores.append(sum(5 ** i * completion_points[char] for i, char in enumerate(line)))

print(total_syntax_error_score)
print(sorted(completion_scores)[len(completion_scores)//2])
