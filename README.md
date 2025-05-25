
𝗔𝗿𝗿𝗮𝘆𝘀
1.Two Sum - https://lnkd.in/dWDJFCrk
2.Best Time to Buy and Sell Stock - https://lnkd.in/dbfXdHcc
3.Maximum Subarray - https://lnkd.in/dA3e79e7
4.Container with Most Water - https://lnkd.in/derBVWA2
5.Rotate Array - https://lnkd.in/d3iAd_ye

𝗦𝘁𝗿𝗶𝗻𝗴𝘀
1.Reverse String - https://lnkd.in/dSYxrHkt
2.Valid Palindrome - https://lnkd.in/dNTpQFit
3.Longest Substring Without Repeating Characters - https://lnkd.in/dMYzuAY4
4.Group Anagrams - https://lnkd.in/dZAMtWYM
5.Longest Palindromic Substring - https://lnkd.in/dnk7bi7m

𝗟𝗶𝗻𝗸𝗲𝗱 𝗟𝗶𝘀𝘁
1.Reverse Linked List - https://lnkd.in/drbzn2b6
2.Merge Two Sorted Lists - https://lnkd.in/d7dPE39P
3.Remove Nth Node From End of List - https://lnkd.in/dhwSrxbu
4.Linked List Cycle - https://lnkd.in/dvymdefx
5.Intersection of Two Linked Lists - https://lnkd.in/dfJKZ2dZ

𝗧𝗿𝗲𝗲𝘀
1.Maximum Depth of Binary Tree - https://lnkd.in/dCMEXszH
2.Validate Binary Search Tree - https://lnkd.in/dZVA-vNR
3.Symmetric Tree - https://lnkd.in/ddx6A8Zw
4.Binary Tree Level Order Traversal - https://lnkd.in/diR5nX4U
5.Lowest Common Ancestor of a Binary Tree - https://lnkd.in/dFkJwkaV

𝗚𝗿𝗮𝗽𝗵𝘀
1.Number of Islands - https://lnkd.in/drj5P3bf
2.Course Schedule - https://lnkd.in/duvfs54r
3.Word Ladder - https://lnkd.in/dmTspiu3
4.Clone Graph - https://lnkd.in/dXYJsBMY
5.Network Delay Time - https://lnkd.in/d3WVx_JP

𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 & 𝗦𝗼𝗿𝘁𝗶𝗻𝗴
1.Merge Sort - https://lnkd.in/d5TVqNCE
2.Quick Sort - https://lnkd.in/d5TVqNCE
3.Binary Search - https://lnkd.in/dQNu5M-V
4.Search in Rotated Sorted Array - https://lnkd.in/dWMGpD5e
5.First Bad Version - https://lnkd.in/dBpRdqwt

𝗗𝘆𝗻𝗮𝗺𝗶𝗰 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗶𝗻𝗴
1.Fibonacci Number - https://lnkd.in/dJqY369E
2.Climbing Stairs - https://lnkd.in/dK8UxFsq
3.Longest Increasing Subsequence - https://lnkd.in/dSkJXnDp
4.Maximum Subarray Sum - https://lnkd.in/dA3e79e7
5.Coin Change - https://lnkd.in/d-ByK5Fx
=======
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



