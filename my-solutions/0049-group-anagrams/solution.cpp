class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;

        for (const auto& x : strs) {
            string word = x;

            sort(word.begin(), word.end());

            mp[word].push_back(x);
        }

        vector<vector<string>> ans;
        ans.reserve(mp.size());
        for (auto& entry : mp) {
            ans.push_back(std::move(entry.second));
        }
        return ans;
    }
};
