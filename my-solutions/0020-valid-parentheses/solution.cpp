class Solution {
public:
    bool isValid(string s) {
        vector<char> st = {};

        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {st.push_back(c);}
            else if (c == ')') {
                if (st.empty() || st.back() != '(') {return false;}
                else {st.pop_back();}
            } else if (c == '}') {
                if (st.empty() || st.back() != '{') {return false;}
                else {st.pop_back();}
            } else if (c == ']') {
                if (st.empty() || st.back() != '[') {return false;}
                else {st.pop_back();}
            }
        }

        return st.empty();
    }
};
