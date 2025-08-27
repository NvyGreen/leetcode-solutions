class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;

        for (auto& token: tokens) {
            if (token == "+" && st.size() >= 2) {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                st.push(a + b);
            } 
            else if (token == "-" && st.size() >= 2) {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                st.push(a - b);
            } 
            else if (token == "*" && st.size() >= 2) {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                st.push(a * b);
            } 
            else if (token == "/" && st.size() >= 2) {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                st.push(a / b);
            } 
            else {
                st.push(stoi(token));
            }
        }

        return st.top();
    }
};
