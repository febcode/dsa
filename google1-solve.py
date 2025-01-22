# input:
# connections = [1, 2, 4, 4, -1]
# rating = [2, 3, 1, 4, 0]
# k=2

#     4
#    / \
#   2   3
#  /     \
# 1       0 
# Execution:
# Starting at the root (4):
# Node 4 has children 2 and 3.
# Explore child 2, then its child 1 (path: 4 → 2 → 1).
# Explore child 3 (path: 4 → 3).
# Result:
# Max path rating: 
# 4+3+0=7 (path 4 → 3).


# 1. Understanding the Problem as a Graph
# Concept: The connections array represents a tree-like graph structure. 
# Each node is connected to its parent, and we need to traverse the graph to maximize the path ratings.
# Key DSA: Adjacency list representation of a graph and tree traversal (DFS or BFS).

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
connections = [1, 2, 4, 4, -1]
rating = [2, 3, 1, 4, 0]

from collections import defaultdict

# Step 1: Build adjacency list
graph = defaultdict(list)
root = -1
for child, parent in enumerate(connections):
    print(str(child) + "--child")
  
    print(str(parent) + '--parent')
    
#     0--child
# 1--parent
# 1--child
# 2--parent
# 2--child
# 4--parent
# 3--child
# 4--parent
# 4--child
# -1--parent
   
    if parent == -1:
        root = child  # Identify the root
    else:
        graph[parent].append(child)

print(graph)  # Adjacency list representation
# Output: {1: [0], 2: [1], 4: [2, 3], -1: []}

# 2. Traversing the Tree
# Concept: We need to traverse the tree to explore all valid paths.
# Use DFS (Depth-First Search) to explore paths recursively.
# Path Length Constraint: Stop traversal when the path length exceeds k.

def dfs(node, path_length, k, graph, visited):
    if path_length > k:  # Stop if path length exceeds k
        return 0

    # Print visited node and current path length
    print(f"Visiting node {node}, path length: {path_length}")
    max_rating = 0
    for child in graph[node]:
        max_rating = max(max_rating, dfs(child, path_length + 1, k, graph, visited))
    
    return max_rating + rating[node]

# Example usage
visited = set()
k = 2
print(dfs(root, 1, k, graph, visited))
# Output: Traverses the tree and returns the maximum rating """


# 3. Using a Heap for Top k Ratings
# Concept: A min-heap can store the top k ratings at each node efficiently. 
# This helps in tracking the best k child paths.

import heapq

def dfs_with_heap(node, path_length, k, graph):
    if path_length > k:  # Stop if path length exceeds k
        return 0

    max_heap = []
    for child in graph[node]:
        child_rating = dfs_with_heap(child, path_length + 1, k, graph)
        heapq.heappush(max_heap, child_rating)
        if len(max_heap) > k:  # Keep only top k ratings
            heapq.heappop(max_heap)

    # Sum the top k ratings and add the current node's rating
    best_ratings = sum(max_heap)
    return rating[node] + best_ratings
k = 2
# print(dfs_with_heap(root, 1, k, graph))
# Output: Returns the maximum rating along a valid path


# 4. Dynamic Programming (Optional Enhancement)
# Concept: Use DP to store the maximum rating at each node for a given path length. This avoids recomputation and improves efficiency.
# Key DSA: Multi-dimensional DP table.
# Example: Dynamic Programming

def dfs_with_dp(node, path_length, dp, k, graph):
    if path_length > k:
        return 0

    # Check if already computed
    if dp[node][path_length] != -1:
        return dp[node][path_length]

    max_rating = 0
    print(str(node)+ 'node')
    for child in graph[node]:
        print(str(child) + 'child' )
        max_rating = max(max_rating, dfs_with_dp(child, path_length + 1, dp, k, graph))
    
    # Store result in DP table
    dp[node][path_length] = rating[node] + max_rating
    
    print(dp)
    # [[-1, -1, -1], [-1, -1, -1], [-1, -1, 1], [-1, -1, 4], [-1, 4, -1]]
    return dp[node][path_length]

# Initialize DP table
n = len(connections)
dp = [[-1] * (k + 1) for _ in range(n)]
print(dp)
# [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
print(dfs_with_dp(root, 1, dp, k, graph))
# Output: Maximum rating using dynamic programming


# 5. Combining the Concepts
# To solve the problem:

# Graph Construction: Build the adjacency list.
# DFS Traversal: Explore all valid paths recursively.
# Heap for Top k: Maintain only the best k ratings.
# Dynamic Programming (Optional): Cache intermediate results for efficiency.


# Summary of Key DSAs Used
# DSA Concept	            Usage
# Graph Representation	Adjacency list for parent-child relationships.
# Tree Traversal (DFS)	Explore paths from the root to leaves while respecting constraints.
# Heap (Priority Queue)	Track top k ratings efficiently at each node.
# Dynamic Programming	    Store intermediate results to avoid recomputation (optional).



