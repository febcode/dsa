# Recursion & Backtracking

Recursion breaks a problem into smaller sub-problems, while backtracking is all about exploring possibilities and undoing wrong paths. These are key in solving puzzles, generating combinations, and navigating decision trees.

4.1. Generate All Subsets (Power Set)

Example:
Input: [1, 2]
Output: [[], [1], [2], [1,2]]

Solution:
Use recursion to decide at each step whether to include the current number or not. This forms a decision tree.

Concept tested:
Your ability to build all possible combinations using recursion and backtrack to try alternate paths.

4.2. String Permutations

Example:
Input: "abc"
Output: "abc", "acb", "bac", "bca", "cab", "cba"

Solution:
Swap characters at different positions recursively. Backtrack to restore original state after each recursive call.

Why it’s asked:
Tests your grasp on recursion and how you track used elements, handle duplicates, and manage state restoration.


4.3. Sudoku Solver

Example:
Given a partially filled 9x9 Sudoku board, fill it so that every row, column, and box has digits 1 to 9.

Solution:
Use recursion to try valid digits for each empty cell. If a choice leads to dead-end, backtrack and try the next.

Concept tested:
Constraint-based recursion with pruning. A great example of advanced backtracking.


4.4. N-Queens Problem

Example:
Place N queens on an N×N chessboard such that no two queens attack each other.

Solution:
Place a queen row by row, checking for conflicts. Backtrack if a valid placement isn’t possible.

Why it’s asked:
Classic CS problem that tests board recursion, pruning, and optimization.


4.5. Word Search in a Grid

Example:
Search for a word like "CAT" in a 2D board where each move can go up, down, left, or right.

Solution:
Start at each cell, recursively explore neighbors, and backtrack if the path doesn’t match the word.

Concept tested:
Grid-based recursion and path validation — common in game-related problems.


To master recursion, imagine each decision as a branch in a tree — each function call leads to the next. Backtracking builds on this by exploring one path, and if it doesn't work, going back to try another path.
