nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6] 
n = 3

# nums1 = [4,5,6,0,0,0]
# nums2= [1,2,3]

nums1 = [1]
m = 1
nums2 = []
n = 0


nums1 = [0]
m = 0
nums2 = [1]
n = 1

nums1 = [4,0,0,0,0,0]
m = 1
nums2= [1,2,3,5,6]
n = 5
def merge( nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1 = [4,0,0,0,0,0]
    nums2= [1,2,3,5,6]
    sum = (m + n) 
    i = 0 
    j = 0 
    
    for i in range(sum):
        if(n!= 0): 
            if j < m :  
                if nums1[i] > nums2[j]  :
                    nums1[i] , nums2[j] = nums2[j] , nums1[i]
                    if j < m-1:
                        if nums2[j] > nums2[j+1] :
                            j = j+1
                if nums1[i] < nums2[j] :
            
                    if nums1[i] == 0 and m != 0:
                        print('in 000')
                        a = i
                        b = 0
                        for l in range(len(nums2)):
                            nums1[a] , nums2[b]  = nums2[b] , nums1[a]
                            b = b+1
                            a = a+1
                            
                            
                        break
                            
                        # resetzero(nums1,nums2,i,0)
                    else:
                        nums1, nums2 = nums2 , nums1
                       
              
            
        
            i = i+1      
 
        
    
        print('*******')
        print(nums1)
        print(nums2)
        print('*******')


def resetzero (nums1,nums2,a ,b):
    
    for n in range(len(nums2)):
        nums1[a] , nums2[b]  = nums2[b] , nums1[a]
        b = b+1
        a = a+1 
        
    return nums1
    
# merge(nums1, m, nums2, n)

# Time Complexity:
# 𝑂(𝑚+𝑛)
# O(m+n), because we iterate through both arrays once.

# Space Complexity:
# 𝑂(1)
# O(1), as the merging is done in-place in nums1.


# The idea of starting from the end (reverse order) avoids overwriting elements in nums1.
# Edge cases to handle:
# If nums2 is empty, no merging is needed.
# If nums1 is initially empty (m = 0), directly copy elements from nums2.
# This is a common two-pointer technique problem and highlights efficient in-place array manipulation.

def newmerge(nums1 , m , nums2, n):
    p1, p2, p = m-1 , n-1 , m+n- 1 
    
    while(p1>= 0 and p2 >=0):
        if nums1[p1]>nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1   
          
       
        
        
    while(p2 >= 0):
        nums1[p] = nums2[p2]
        p2 -= 1
        
        p -= 1
    print(nums1)
   


newmerge(nums1, m, nums2, n)