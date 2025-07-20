class Solution {
public:
    int maxVowels(string s, int k) {
        int max_vowels = 0;
        int curr_vowels = 0;
        string vowels = "aeiou";

        for (int i = 0; i < k; ++i) {
            if (vowels.find(s[i]) != string::npos) {
                ++curr_vowels;
            }
        }
        max_vowels = curr_vowels;

        for (int i = k; s[i] != '\0'; ++i) {
            if (vowels.find(s[i - k]) != string::npos) {
                --curr_vowels;
            }

            if (vowels.find(s[i]) != string::npos) {
                ++curr_vowels;
            }

            max_vowels = max(curr_vowels, max_vowels);
        }

        return max_vowels;
    }
};
