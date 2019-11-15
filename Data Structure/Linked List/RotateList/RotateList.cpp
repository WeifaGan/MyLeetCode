class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(k==0||head==NULL) return  head;
        if(head->next==NULL) return head;
        ListNode* p_end=head;
        ListNode* p_pre=head;
        int num_node=1;
        while(p_end->next!=NULL)
        {
            p_end=p_end->next;
            num_node++;
        }
        
        if(k%num_node==0) return head;
        int n=num_node-k%num_node;
 

        for(int i=1;i<n;i++)
        {
            p_pre=p_pre->next;
        }
        ListNode* p_head=p_pre->next;
        p_end->next=head;
        p_pre->next=NULL;
        
        return p_head;
        
    }
};
