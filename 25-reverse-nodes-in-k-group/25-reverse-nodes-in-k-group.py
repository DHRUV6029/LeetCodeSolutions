# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(st):
            point = curhead =ListNode(0)
            while st:
                point.next = st.pop()
                point =point.next
            point.next = None
    
            return curhead.next
    
        st=[]
        c=0
        cur = head
        newHead = dummyhead =ListNode(0)
    
        while cur:
            st.append(cur)
            cur = cur.next
            c+=1

            if c==k:
                khead = reverse(st)
            
                newHead.next = khead
                while newHead.next:
                    newHead =newHead.next
                c=0

        while st:
            newHead.next = st.pop(0)
            newHead = newHead.next
    
        newHead.next = None
        return dummyhead.next
        
        