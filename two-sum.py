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
# print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]


from collections import Counter

def first_unique_char(s):
    count = Counter(s)
    # print(count)
    for i, char in enumerate(s):
        if count[char] == 1:
            print(i)
            return i
    return -1

# Example usage:
print(first_unique_char("leetcode"))  # Output: 0