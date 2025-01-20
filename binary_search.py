## Key Points
# Precondition: The array must be sorted in ascending or descending order.
# Divide and Conquer: The algorithm divides the search space into two parts, and only one part is considered for the next step.
# Efficiency: It has a time complexity of 𝑂(log 𝑛) making it much faster than linear search O(n)) for large arrays.

## How Binary Search Works
# Initialization:

# Start with two pointers:
# left pointing to the beginning of the array 0.
# right pointing to the end of the array (𝑛−1)

# Midpoint Calculation:
# Compute the middle index:
# mid = left + (right− left) / 2

# Comparison:

# If the value at mid is the target, return mid.
# If the target is less than the value at mid, adjust right to mid - 1.
# If the target is greater than the value at mid, adjust left to mid + 1.
# Repeat:
# Continue the process until left > right (indicating the target is not in the array).


def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow in large numbers
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found


def binary_search_recursive(nums, target, left, right):
    if left > right:
        return -1  # Base case: target not found
    
    mid = left + (right - left) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


# Applications of Binary Search
# 1. Searching in a sorted array or list.
# 2. Finding the first or last occurrence of a target in a sorted array.
# 3. Solving problems like:
#     Square root of a number.
#     Finding a peak element in an array.
#     Searching in rotated sorted arrays.


