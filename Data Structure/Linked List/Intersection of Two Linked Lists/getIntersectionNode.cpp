/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        set<ListNode *>myset;
     
        while(headA)
        {
            myset.insert(headA);
            headA=headA->next;
          
        }
        
        while(headB)
        {
            if(myset.find(headB)!=myset.end())
            {return headB;}
            else{headB=headB->next;}
        }
        return NULL;
    }    
};
