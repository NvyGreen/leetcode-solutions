class Solution {
public:
    string predictPartyVictory(string senate) {
        int senate_size = senate.size();
        queue<int> rad;
        queue<int> dir;

        for (int i = 0; senate[i] != '\0'; ++i) {
            if (senate[i] == 'R') {
                rad.push(i);
            } else {
                dir.push(i);
            }
        }

        while (!dir.empty() && !rad.empty()) {
            if (dir.front() < rad.front()) {
                dir.push(senate_size++);
            } else {
                rad.push(senate_size++);
            }

            dir.pop();
            rad.pop();
        }

        if (rad.size() == 0) {
            return "Dire";
        } else {
            return "Radiant";
        }
    }
};
