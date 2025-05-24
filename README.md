# dsa
*Most Asked Programming Interview Questions with Detailed Answers*

*Arrays*

*1. How is an array sorted using quicksort?* 

Quicksort is a divide-and-conquer algorithm:

1. Pick a pivot.

2. Partition the array so that elements < pivot go left, > pivot go right.

3. Recursively apply quicksort to left and right subarrays.

*Time Complexity: Avg - O(n log n), Worst - O(n^2), Space - O(log n).*


*2. How do you reverse an array?*

Initialize two pointers at the start and end.

Swap elements at those pointers.

Move start forward and end backward until they meet.


*3. How do you remove duplicates from an array?*

For unsorted: Use a hash set to track seen elements.

For sorted: Traverse, skip if current equals previous.


*4. How do you find the 2nd largest number in an unsorted integer array?*

Initialize two variables: first, second.

Traverse array:

If current > first, update both first and second.

Else if current > second and != first, update second.


*Linked Lists*

*1. How do you find the length of a linked list?*

Initialize a counter, traverse the list, increment counter until null.


*2. How do you reverse a linked list?*

Use three pointers: prev, current, next.

Iterate: point current.next to prev, move pointers ahead.



*3. How do you find the third node from the end?*

Use two pointers with a gap of 3 nodes. Move both until end is reached.



*4. How are duplicate nodes removed in an unsorted linked list?*

Use a hash set to track seen data.

Traverse and remove node if data already exists in the set.


*Strings*

*1. How do you check if a string contains only digits?*

Use regex: str.matches("\\d+") in Java.

Or loop through each char and check with Character.isDigit().


*2. How can a given string be reversed?*

Convert to char array and swap start and end.

Or use StringBuilder(str).reverse() in Java.



*3. How do you find the first non-repeated character?*

Use a LinkedHashMap to store frequency.

Traverse again to return the first with frequency 1.



*4. How do you find duplicate characters in strings?*

Use a HashMap to count frequency of each char.

Return chars with count > 1.


*Binary Trees*

*1. How are all leaves of a binary tree printed?*

Traverse recursively.

If node has no left and right child, print it.


*2. How do you check if a tree is a binary search tree?*

Recursively ensure all nodes lie within valid range (min < node < max).



*3. How is a binary search tree implemented?*

Each node has left, right, and data.

Insert: If value < node, go left, else right.

Search: Same logic.



*4. Find the lowest common ancestor in a binary tree?*

If root is null or matches one node, return root.

Recurse left and right.

If both sides return non-null, root is LCA.


*Graph*

*1. How to detect a cycle in a directed graph?*

Use DFS with recursion stack.

If a node is revisited in the same stack path, cycle exists.



*2. How to detect a cycle in an undirected graph?*

Use DFS/BFS with visited set.

Track parent; if visited neighbor is not parent, cycle exists.



*3. Find the total number of strongly connected components?*

Use Kosaraju’s algorithm:

DFS and push to stack.

Reverse graph.

DFS in order of stack to count components.



*4. Find whether a path exists between two nodes of a graph?*

Use DFS/BFS to check if end is reachable from start.



*5. Find the minimum number of swaps required to sort an array.*

- Use cycle detection:

- Pair values with original indices.

- Sort based on values.

- Count cycles in the new index positions.

- For each cycle of size n, swaps = n-1.


*Dynamic Programming*

*1. Find the longest common subsequence?*

Use DP table dp[i][j] where:

dp[i][j] = dp[i-1][j-1]+1 if s1[i-1]==s2[j-1]

Else max of dp[i-1][j] and dp[i][j-1]


*2. Find the longest common substring?*

Similar to LCS but:

dp[i][j] = dp[i-1][j-1]+1 if match else 0.

Keep track of max length.


*3. Coin change problem?*

Use DP array dp[amount+1].

dp[0]=0; for each coin and amount, update dp[i] = min(dp[i], dp[i-coin]+1)


*4. Box stacking problem?*

Treat each rotation as a separate box.

Sort by base area (width * depth).

Use DP to find max stack height like LIS (Longest Increasing Subsequence).


*5. Count the number of ways to cover a distance?*

Use DP: ways[n] = ways[n-1] + ways[n-2] + ways[n-3]

Base cases: ways[0]=1, ways[1]=1, ways[2]=2


React with ❤️ for more interview resources