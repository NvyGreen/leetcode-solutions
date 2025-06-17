class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        if (nums.size() == 2) {
            return vector<int>{0, 1};
        }

        map<int, int> index_of_val;    // first = index, second = value

        for (int i = 0; i < nums.size(); ++i) {
            int diff = target - nums[i];
            auto map_it = find_if(index_of_val.begin(), index_of_val.end(), [&diff](auto record) {return record.second == diff;});

            if (map_it == index_of_val.end()) {
                index_of_val.insert(make_pair(i, nums[i]));
            } else {
                return vector<int>{map_it->first, i};
            }
        }

        // for (int i = 0; i < nums.size(); ++i) {
        //     for (int j = i + 1; j < nums.size(); ++j) {
        //         if (nums[i] + nums[j] == target) {
        //             return vector<int>{i, j};
        //         }
        //     }
        // }

        return vector<int>{0, 1};
    }
};
