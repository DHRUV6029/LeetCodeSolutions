# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:        
        nodeMap = defaultdict()
        
        cur = head
        while cur:
            if cur.val not in nodeMap:
                nodeMap[cur.val]=1
            else:
                
            
                nodeMap[cur.val] = -1
            cur = cur.next
        
        point = head = ListNode(0)
        for k ,v in nodeMap.items():
            if v==1:
                point.next = ListNode(k)
                point  =point.next
        point.next = None
        return head.next
        