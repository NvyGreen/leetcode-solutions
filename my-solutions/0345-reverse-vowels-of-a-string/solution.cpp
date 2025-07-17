class Solution {
public:
    string reverseVowels(string s) {
        string vowels = "aeiou";
        int head = 0;
        int tail = s.size() - 1;

        while (head < tail) {
            if (vowels.find(tolower(s[head])) != string::npos) {
                while (vowels.find(tolower(s[tail])) == string::npos) {
                    --tail;
                }
                char temp = s[head];
                s[head] = s[tail];
                s[tail] = temp;
            }
            else if (vowels.find(tolower(s[tail])) != string::npos) {
                while (vowels.find(tolower(s[head])) == string::npos) {
                    ++head;
                }
                char temp = s[head];
                s[head] = s[tail];
                s[tail] = temp;
            }

            ++head;
            --tail;
        }

        return s;
    }
};
