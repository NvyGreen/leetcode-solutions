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
    ListNode* rotateRight(ListNode* head, int k) {
        ListNode* curr = head;
        if (k == 0 || head == nullptr || head -> next == nullptr) return head;

        int cnt = 1;
        while(curr -> next != nullptr) {
            cnt++;
            curr = curr -> next;
        }
        curr -> next = head;

        k %= cnt;
        int same = abs(k - cnt);
        curr = head;

        for (int i = 1; i < same; i++) {
            curr = curr -> next;
        }

        head = curr -> next;
        curr -> next = nullptr;

        return head;
    }
};
