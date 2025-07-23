class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        vector<int> pairs;
        sort(potions.begin(), potions.end());

        for (int spell : spells) {
            int suc_potions = 0;

            int low = 0;
            int high = potions.size() - 1;
            while (low <= high) {
                int mid = (low + high) / 2;
                long long strength = (long long)spell * (long long)potions[mid];

                if (strength >= success) {
                    suc_potions += (potions.size() - mid - suc_potions);
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }

            pairs.push_back(suc_potions);
        }

        return pairs;
    }
};
