data = "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010"

with open("inputs/3.txt") as file:
    data = file.read()

nums = data.splitlines()

def bin_list_to_dec(bin_list:list) -> int:
  return int("".join(str(i) for i in bin_list), 2)


# Part 1
counts_of_one = [sum(int(number[bit_index]) for number in nums) for bit_index in range(len(nums[0]))]
gamma = [1 if count > len(nums)/2 else 0 for count in counts_of_one]
epsilon = [int(not bit) for bit in gamma]

print("Part 1: ", bin_list_to_dec(gamma) * bin_list_to_dec(epsilon))

# Part 2
possible_oxygen = [list(n) for n in nums]
for index in range(len(nums[0])):
  bits = [num[index] for num in possible_oxygen]
  char_to_keep = '0' if bits.count('0') > bits.count('1') else '1'
  possible_oxygen = [n for n in possible_oxygen if n[index] == char_to_keep]
  if len(possible_oxygen) == 1:
    break

possible_co2 = [list(n) for n in nums]
for index in range(len(nums[0])):
  bits = [num[index] for num in possible_co2]
  char_to_keep = '0' if bits.count('0') <= bits.count('1') else '1'
  possible_co2 = [n for n in possible_co2 if n[index] == char_to_keep]
  if len(possible_co2) == 1:
    break

print("Part 2: ", bin_list_to_dec(possible_oxygen[0]) * bin_list_to_dec(possible_co2[0]))

