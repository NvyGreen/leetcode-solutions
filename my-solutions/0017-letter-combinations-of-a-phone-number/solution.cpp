class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) {
            return {};
        }

        unordered_map<char, string> phoneMapping = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };

        vector<string> result;
        string current;

        backtrack(0, digits, phoneMapping, current, result);
        return result;
    }

private:
    void backtrack(int index, const string& digits, unordered_map<char, string>& mapping, string& current, vector<string>& result) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }

        for (char c : mapping[digits[index]]) {
            current.push_back(c);
            backtrack(index + 1, digits, mapping, current, result);
            current.pop_back();
        }
    }
};
