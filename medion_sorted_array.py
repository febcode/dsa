def find_median_sorted_arrays(nums1, nums2) :
    nums = sorted(nums1 + nums2)
    print(nums)
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        print('here')
        return (nums[n // 2 - 1] + nums[n // 2]) / 2

# Example Usage
print(find_median_sorted_arrays([1, 3,4,8], [2,8,9,10]))  # Output: 2.0

