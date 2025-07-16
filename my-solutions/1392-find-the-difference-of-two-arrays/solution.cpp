class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        set<int> only1;
        set<int> only2;
        set<int> inBoth;

        for (int i = 0; i < nums1.size(); ++i) {
            auto found_it = find(nums2.begin(), nums2.end(), nums1[i]);
            if (found_it != nums2.end()) {
                inBoth.insert(nums1[i]);
            } else {
                only1.insert(nums1[i]);
            }
        }

        for (int i = 0; i < nums2.size(); ++i) {
            auto found_it = find(inBoth.begin(), inBoth.end(), nums2[i]);
            if (found_it == inBoth.end()) {
                only2.insert(nums2[i]);
            }
        }

        vector<vector<int>> total = {vector<int>(only1.begin(), only1.end()), vector<int>(only2.begin(), only2.end())};
        return total;
    }
};
