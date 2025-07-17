class Solution {
public:
    bool isSubsequence(string s, string t) {
        string v = "";
        int j = 0;

        for (int i = 0; i < t.size(); ++i) {
            if (j < s.size() && t[i] == s[j]) {
                v += t[i];
                ++j;
            }
        }

        return v == s;
    }
};
