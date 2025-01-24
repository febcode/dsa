def max_subarray(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        print(num)
        max_current = max(num, max_current + num)
        print(str(max_current)+'maxc' )
        max_global = max(max_global, max_current)
        print(str(max_global)+'maxg' )
    return max_global

# Example Usage
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
