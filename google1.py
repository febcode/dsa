# resort hills rating problem from google 
# we can go from bottom to top 
# top to bottom we can not come 

# we can cover k path only 


#        4 
#       / \
#      /   3
#     2
#    /
#   /
#  1
#  /
# /
# 0

# 0 -> 1 = 2 rating
# 1 ->2 = 3 rating
# 2 -> 4 = 1  rating
# 3 ->4 = 4  rating

connections = [1,2,4,4,-1]
rating = [2,3,1,4,0]

import heapq
k = 2
def getmaxRating(connections , rating):
    min_heap = []
    for i in range(len(connections)):
        if(connections[i-1]!= connections[i] and connections[i-1] <= connections[i]):
            heapq.heappush(min_heap, rating[i])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        print(min_heap)
    return min_heap[0]
    
getmaxRating(connections , rating)

# function nahi banaya
# heap pop and heappush function wrong 
# not sure how loop was applied range(len(connections))