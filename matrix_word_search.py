def word_search(board, word) :
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False

        # Mark the cell as visited
        print()
        temp, board[r][c] = board[r][c], '#'
        found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or 
                 dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
        board[r][c] = temp  # Unmark the cell
        return found
    
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

# Example Usage
board = [
    ['A','B','C','E'], 
    ['S','F','C','S'], 
    ['A','D','E','E']
    ]
print(word_search(board, "ABCCED"))  # Output: True
