def two_sum(nums, target) -> list:
    num_map = {}  # Dictionary to store number and its index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            print(num_map[complement])
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Example Usage
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]