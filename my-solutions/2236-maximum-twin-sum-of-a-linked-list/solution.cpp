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
    int pairSum(ListNode* head) {
        vector<int> vals;
        for (ListNode* p = head; p != nullptr; p = p->next) {
            vals.push_back(p->val);
        }

        int start = 0;
        int end = vals.size() - 1;
        int max_sum = 0;

        while (start < end) {
            max_sum = max(vals[start] + vals[end], max_sum);
            ++start;
            --end;
        }

        return max_sum;
    }
};
