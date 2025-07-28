class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> remaining;

        for (int asteroid : asteroids) {
            bool destroyed = false;

            while (!remaining.empty() && asteroid < 0 && remaining.back() > 0) {
                if (abs(remaining.back()) < -asteroid) {
                    remaining.pop_back();
                    continue;
                } else if (abs(remaining.back()) == -asteroid) {
                    remaining.pop_back();
                    destroyed = true;
                    break;
                } else {
                    destroyed = true;
                    break;
                }
            }

            if (!destroyed) {
                remaining.push_back(asteroid);
            }
        }

        return remaining;
    }
};
