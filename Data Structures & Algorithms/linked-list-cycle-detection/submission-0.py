# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr = head
        nodes = set()
        while curr:
            if curr.next and curr.next.val in nodes:
                return True
            if curr.next:
                nodes.add(curr.next.val)
            curr = curr.next
        
        return False
        