class Solution {
public:
    string removeStars(string s) {
        string c="";

        for (int i = 0; s[i] != '\0'; ++i) {
            if (s[i] == '*') {
                c.pop_back();
            } else {
                c += s[i];
            }
        }

        return c;
    }
};
