
"""
Do not return anything, modify nums in-place instead.
"""
k = 3
numsn = [1,2,3,4,5,6,7,]
k %= len(numsn)
print(k)

def reverse(left, right):
    print('left')
    print(left)
    print('right')
    print(right)
    while left < right:
        numsn[left], numsn[right] = numsn[right], numsn[left]
        left += 1
        right -= 1
    print(numsn)

reverse(0, len(numsn) - 1)
reverse(0, k - 1)
reverse(k, len(numsn) - 1)
        
       
        
 