# Problem Statement
# Given an integer array nums and an integer k, return the 𝑘
# k-th largest element in the array.

# Key Points:
# Kth Largest Element: It's the 𝑘
# k-th element when the array is sorted in descending order.
# The problem assumes that 𝑘
# k is always valid, meaning 1≤𝑘≤len(nums)


# 1. Sorting
# Sort the array in descending order.
# Return the element at index 
# 𝑘−1

# Time Complexity: 
# O(nlogn), due to sorting.

# Space Complexity: 
# O(1), if the sorting is done in-place.

def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]


# Min-Heap
# Use a min-heap of size 𝑘
# Add elements to the heap, maintaining its size at 𝑘
# by removing the smallest element when the size exceeds 𝑘
# After processing all elements, the root of the heap is the 𝑘
# k-th largest element.
# Time Complexity: 
# O(nlogk), where 𝑛 is the number of elements, and maintaining the heap costs 
# O(logk) per element.
# Space Complexity: 
# O(k), for the heap.

import heapq

def findKthLargestheapq(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
        
        print(min_heap)
    return min_heap[0]


nums = [3,2,1,5,6,4]
k = 2
print(findKthLargestheapq(nums,k))