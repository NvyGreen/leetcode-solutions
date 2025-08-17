class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> mp;
        unordered_map<string, char> rev;
        int left = 0;
        int i = 0;
        int n = pattern.length(), m = s.length();

        while (i < n) {
            if (left >= m) return false;

            int j = left;
            while (j < m && s[j] != ' ') j++;

            string word = s.substr(left, j - left);
            char ch = pattern[i];

            if (mp.count(ch) && mp[ch] != word) return false;
            if (rev.count(word) && rev[word] != ch) return false;

            mp[ch] = word;
            rev[word] = ch;

            left = j + 1;
            i++;
        }

        return left > m;
    }
};
