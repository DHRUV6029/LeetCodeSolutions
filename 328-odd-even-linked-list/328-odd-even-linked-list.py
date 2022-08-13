# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenSt = []
        oddSt = []
        cur = head
        idx = 1

        while cur:
            if idx%2==0:
                evenSt.append(cur)
            else:
                oddSt.append(cur)
            idx+=1
            cur = cur.next
        point = head = ListNode(0)
        #odd first then even
        while oddSt:
            point.next = oddSt.pop(0)
            point = point.next

        while evenSt:
            point.next = evenSt.pop(0)
            point = point.next

        point.next = None
        return head.next