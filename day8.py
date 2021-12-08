values = [[s.split() for s in line.split('|', 2)] for line in open("inputs/8.txt").read().splitlines()]

print(sum(1 for v in values for digit in v[1] if len(digit) in (2, 3, 4, 7)))

def get_output(signals, outputs):
    mapping = {i: None for i in range(1, 10)}
    mapping[1] = next(set(signal) for signal in signals if len(signal) == 2)
    mapping[4] = next(set(signal) for signal in signals if len(signal) == 4)
    mapping[7] = next(set(signal) for signal in signals if len(signal) == 3)
    mapping[8] = next(set(signal) for signal in signals if len(signal) == 7)
    mapping[6] = next(set(signal) for signal in signals if len(signal) == 6 and len(mapping[1] - set(signal)) == 1)
    mapping[3] = next(set(signal) for signal in signals if len(signal) == 5 and not mapping[1]-set(signal))
    mapping[5] = next(set(signal) for signal in signals if len(signal) == 5 and not set(signal) - mapping[6])
    mapping[2] = next(set(signal) for signal in signals if len(signal) == 5 and mapping[1]-set(signal) and len(set(signal) - mapping[6]) == 1)
    mapping[9] = next(set(signal) for signal in signals if len(signal) == 6 and set(signal) not in mapping.values() and not mapping[5] - set(signal))
    mapping[0] = next(set(signal) for signal in signals if len(signal) == 6 and set(signal) not in mapping.values())
    return int(''.join(next(str(key) for key, char_set in mapping.items() if set(output) == char_set) for output in outputs))

print(sum(get_output(*v) for v in values))
