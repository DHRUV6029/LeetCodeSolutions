class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        ListNode* dummy_odd = new ListNode(-1);
        ListNode* dummy_even = new ListNode(-1);
        
        ListNode* odd = dummy_odd;
        ListNode* even = dummy_even;
        
        int n = 0;
        ListNode* curr = head;
        
        while(curr != nullptr){
            n++;
            
            if(n % 2 == 1){
                odd->next = curr;
                odd = odd->next;
            }
            else{
                even->next = curr;
                even = even->next;
            }
            
            curr = curr->next;
        }
        
        even->next = nullptr;
        odd->next = dummy_even->next;
        
        return dummy_odd->next;
    }
};