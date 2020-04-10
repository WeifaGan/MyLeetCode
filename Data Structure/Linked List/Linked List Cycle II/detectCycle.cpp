class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        set<ListNode*> myset;
        while(head)
        {
            if(myset.find(head)!=myset.end())
            {return head;}
            myset.insert(head);
            head=head->next;
        }
        return NULL;
    }
};
