class Solution {
public:
    int strStr(string haystack, string needle) {
        for (int i = 0; haystack[i] != '\0'; ++i) {
            if (haystack[i] == needle[0]) {
                bool found = true;
                for (int j = 1; needle[j] != '\0'; ++j) {
                    if (haystack[i + j] != needle[j]) {
                        found = false;
                        break;
                    }

                    
                }

                if (found) {
                    return i;
                }
            }
        }

        return -1;
    }
};
