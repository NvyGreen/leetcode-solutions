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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *result = nullptr;
        bool carry = false;
        if (l1->val + l2->val < 10) {
            result = new ListNode{l1->val + l2->val};
        } else {
            carry = true;
            result = new ListNode{(l1->val + l2->val) % 10};
        }

        ListNode *p = l1->next;
        ListNode *q = l2->next;
        ListNode *tail = result;

        for(; p != nullptr && q != nullptr; p=p->next, q=q->next) {
            if (carry) {
                if (p->val + q->val + 1 < 10) {
                    carry = false;
                    tail->next = new ListNode{p->val + q->val + 1};
                    tail = tail->next;
                } else {
                    tail->next = new ListNode{(p->val + q->val + 1) % 10};
                    tail = tail->next;
                }
            } else {
                if (p->val + q->val < 10) {
                    tail->next = new ListNode{p->val + q->val};
                    tail = tail->next;
                } else {
                    carry = true;
                    tail->next = new ListNode{(p->val + q->val) % 10};
                    tail = tail->next;
                }
            }
        }

        for(; p != nullptr; p=p->next) {
            if (carry) {
                if (p->val + 1 < 10) {
                    carry = false;
                    tail->next = new ListNode{p->val + 1};
                    tail = tail->next;
                } else {
                    tail->next = new ListNode{(p->val + 1) % 10};
                    tail = tail->next;
                }
            } else {
                tail->next = new ListNode{p->val};
                tail = tail->next;
            }
        }

        for(; q != nullptr; q=q->next) {
            if (carry) {
                if (q->val + 1 < 10) {
                    carry = false;
                    tail->next = new ListNode{q->val + 1};
                    tail = tail->next;
                } else {
                    tail->next = new ListNode{(q->val + 1) % 10};
                    tail = tail->next;
                }
            } else {
                tail->next = new ListNode{q->val};
                tail = tail->next;
            }
        }

        if (carry) {
            tail->next = new ListNode{1};
            tail = tail->next;
        }

        return result;
    }
};
