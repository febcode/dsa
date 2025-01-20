# Iterative Approach
# Use three pointers:

# prev to track the previous node (initially None).
# current to track the current node (starts at head).
# next_node to store the next node temporarily while reversing links.
# Traverse the list and reverse the next pointer of the current node to point to the previous node.

# Move prev and current one step forward.

# When the loop finishes, prev will point to the new head of the reversed list.

class ListNode():
    def __init__(self , val=0 ,next=None):
        self.val = val
        self.next = next 
        
        
def reverseLinklist(head):
    prev_node = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev_node 
        prev_node = current
        current = next_node
    # current.next, current.prev  = current.prev , current.next

    return prev_node  # New head of the reversed list
            


# Complexity Analysis
# Time Complexity:
# O(n): Each node is visited once.Space Complexity:
# Iterative: 
# O(1), as no additional space is used.
# Recursive: 
# O(n), due to the recursion stack.     
      
def recursive_reverse_linklist(head):
    if not head or not head.next:
        return head # Base case: return the last node as the new head
    
    recursive_call = recursive_reverse_linklist(head.next)
    head.next.next = head  # Reverse the link
    head.next = None       # Prevent cycles
    return recursive_call


# Helper functions to create and print linked lists
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    print(" → ".join(map(str, values)))

# Example usage
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

print("Original linked list:")
print_linked_list(head)

# Reverse the linked list (iterative)
reversed_head = reverseLinklist(head)
print("\nReversed linked list (Iterative):")
print_linked_list(reversed_head)

# Re-create the list and reverse it again (recursive)
head = create_linked_list(values)
reversed_head_recursive = recursive_reverse_linklist(head)
print("\nReversed linked list (Recursive):")
print_linked_list(reversed_head_recursive)       
    
# Explanation of Code Flow
# Create a linked list:

# Use create_linked_list([1, 2, 3, 4, 5]) to create a linked list with values [1, 2, 3, 4, 5].
# Print the original linked list:

# Use print_linked_list(head) to see the original list.
# Reverse the linked list:

# Call reverseList(head) for the iterative method or reverseListRecursive(head) for the recursive method.
# Print the reversed linked list:

# Use print_linked_list(reversed_head) or print_linked_list(reversed_head_recursive).
