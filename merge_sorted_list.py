class LinkNode:
    def __init__(self ,val = 0 ,next = None):
        self.val = val
        self.next = next


def merge_list(l1,l2):
    dummy = LinkNode()
    curr = dummy

    while(l1 & l2):
        if(l1.val < l2.val):
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l1.next
        curr = curr.next

    curr.next = l1 or l2
    return dummy.next
