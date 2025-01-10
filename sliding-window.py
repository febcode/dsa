# find the length of the longest subarray whose sum is less than or equal to k.
# ans = [4,2,1,1] no answer
nums = [3,1,2,7,4,2,1,1,5]
k = 8 

def find_length(nums, k):
    # curr is the current sum of the window
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
        print(ans)
    
    return ans

# find_length(nums, k)

# Example 2: You are given a binary string s (a string containing only "0" and "1"). 
# You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

# For example, given s = "1101100111", the answer is 5. 
# If you perform the flip at index 2, the string becomes 1111100111.
s = [1,1,0,0,1,0,1,1]
def find_length_of_zeros(s):
    # curr is the current number of zeros in the window
    left = curr = ans = 0 
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans

# print(find_length_of_zeros(s))


# Example 3: 713. Subarray Product Less Than K.
# Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.
# For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. 
# The subarrays with products less than k are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]


def numSubarrayProductLessThanK( nums, k) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
                
            ans += right - left + 1

        return ans
    
print(numSubarrayProductLessThanK(nums = [10, 5, 2, 6],k = 100))


# Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
k = 4 
nums = [3,-1,4,12,-8,5,6]
def find_best_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    
    return ans

print(find_best_subarray(nums,k))

# https://leetcode.com/discuss/interview-question/352460/Google-Online-Assessment-Questions