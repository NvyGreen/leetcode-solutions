class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        map<int, int> occurences_map;

        for (const int& num : arr) {
            ++occurences_map[num];
        }

        vector<int> occur;
        for (const auto& [num, freq] : occurences_map) {
            if (find(occur.begin(), occur.end(), freq) != occur.end()) {
                return false;
            } else {
                occur.push_back(freq);
            }
        }

        return true;
    }
};
