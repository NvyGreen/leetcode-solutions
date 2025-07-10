class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string merged_word = "";
        int i = 0;

        for (; word1[i] != '\0' && word2[i] != '\0'; ++i) {
            merged_word = merged_word + word1[i] + word2[i];
        }

        if (word1[i] != '\0') {
            merged_word = merged_word + word1.substr(i);
        } else if (word2[i] != '\0') {
            merged_word = merged_word + word2.substr(i);
        }

        return merged_word;
    }
};
