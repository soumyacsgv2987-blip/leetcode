# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy head node to build the new linked list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Loop while there are nodes to process or a carry remains
        while l1 or l2 or carry:
            # Get values from current nodes, or 0 if we reached the end of a list
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create a new node with the single digit and attach it
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next