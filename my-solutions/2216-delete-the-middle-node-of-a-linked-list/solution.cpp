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
    ListNode* deleteMiddle(ListNode* head) {
        if (head->next == nullptr) {
            return nullptr;
        }

        int mid = 0;
        for (ListNode* p = head; p != nullptr; p = p->next) {
            ++mid;
        }
        mid /= 2;

        ListNode* prev_node = head;
        int i = 0;
        while (i < (mid - 1)) {
            prev_node = prev_node->next;
            ++i;
        }
        ListNode* mid_node = prev_node->next;
        prev_node->next = mid_node->next;
        delete mid_node;

        return head;
    }
};
