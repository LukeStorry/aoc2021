with open("inputs/1.txt") as file:
    data = file.read()

# data = "199\n200\n208\n210\n200\n207\n240\n269\n260\n263"
nums = data.splitlines()

## Part 1
print(sum(1 for x,y in zip(data.splitlines(), data.splitlines()[1:]) if x<y))


## Part 2
window_measurements = [x+y+z for x,y,z in zip(nums, nums[1:], nums[2:])]
count_windows = sum(1 for x,y in zip(window_measurements, window_measurements[1:]) if x<y)
print(f"Part 2: {count_windows}")
