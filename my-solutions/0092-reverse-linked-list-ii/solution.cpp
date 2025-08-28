/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode *l=dummy,*r=dummy,*p=NULL;
        if(left==right) return head;

        for(int i=0;i<left;i++) {
            if(l->next==NULL) break;
            p=l;
            l = l->next;
        }
        for(int i=0;i<right;i++){
            if(r->next==NULL) break;
            r = r->next;
        }
        ListNode * rr = r->next;

        ListNode *prev=l;
        ListNode *curr = prev->next;
        while(prev!=r){
            ListNode *n = curr->next;
            curr->next=prev;
            prev = curr;
            curr = n;
        }
        p->next=r;
        l->next=rr;
        return dummy->next;
    }
};
