# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        cur = head
        carry = 0
        a = 0
        b = 0 
        while l1 is not None or l2 is not None:
            
            if l1 is None:
                a = 0
            else:
                a = l1.val
                
            if l2 is None:
                b= 0
            else:
                b = l2.val
            
            
            s = a + b + carry
             
            
            carry = s//10
            cur.next = ListNode(s%10)
            cur = cur.next
            
            if l1:
                l1 = l1.next
                
            if l2:
                l2=l2.next
                
        if carry > 0:
            cur.next = ListNode(carry)
            cur = cur.next
                
        
        return head.next
                
                