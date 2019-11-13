class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head==NULL)return NULL;
        ListNode* headpt=head;
        ListNode* headpt2;
        ListNode* headpt1=headpt->next;
        if(headpt1!=NULL)headpt2=headpt1->next;
        else{return headpt;}
        head->next=NULL;//头指针反向
        while(true)
        {
            
         headpt1->next=headpt;
         headpt=headpt1;
         headpt1=headpt2;
         if(headpt2!=NULL)
         {headpt2=headpt2->next;}
         else{break;}
        
        }
        // head=headpt1;
        
        return headpt;
    }
};
