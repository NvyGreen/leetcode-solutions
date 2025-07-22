class Solution {
public:
    int compress(vector<char>& chars) {
        char group_char = '\0';
        int group_count = 0;
        int comp_pos = 0;

        for (int i = 0; i < chars.size(); ++i) {
            if (chars[i] != group_char) {
                if (group_char != '\0') {
                    chars[comp_pos] = group_char;
                    if (group_count > 1) {
                        string count_str = to_string(group_count);
                        for (char digit : count_str) {
                            chars[++comp_pos] = digit;
                        }
                    }
                    ++comp_pos;
                }
                
                group_char = chars[i];
                group_count = 1;
            } else {
                ++group_count;
            }
        }

        chars[comp_pos] = group_char;
        if (group_count > 1) {
            string count_str = to_string(group_count);
            for (char digit : count_str) {
                chars[++comp_pos] = digit;
            }
        }
        ++comp_pos;

        return comp_pos;
    }
};
