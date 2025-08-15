class Solution {
public:
    bool isPalindrome(string s) {
        transform(s.begin(), s.end(), s.begin(), [](unsigned char c){ return tolower(c); });
        s.erase(remove_if(s.begin(), s.end(), [](char c){ return !std::isalnum(c); }), s.end());

        string rev = s;
        reverse(rev.begin(), rev.end());

        return s == rev;
    }
};
