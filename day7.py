nums = list(map(int, open("inputs/7.txt").read().split(',')))

print(min(sum(abs(n-position) for n in nums) for position in range(min(nums), max(nums))))
print(min(sum(sum(range(abs(n-position)+1)) for n in nums) for position in range(min(nums), max(nums))))
