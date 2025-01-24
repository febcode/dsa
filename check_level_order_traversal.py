from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    print(root)
    queue = deque([root])
    print(queue)
    while queue:
        level = []
        print(range(len(queue)))
        for _ in range(len(queue)):
            node = queue.popleft()
            print(str(node.val)+'val')
            print(str(node.left)+'left')
            print(str(node.right)+'right')
            level.append(node.val)
            print(level)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            print(result)
        result.append(level)
    
    return result

# Example Usage
# Tree:    1
#         / \
#        2   3
#       / \
#      4   5
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(level_order_traversal(root))  # Output: [[1], [2, 3], [4, 5]]
