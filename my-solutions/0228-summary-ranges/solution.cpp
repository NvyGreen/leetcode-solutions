class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> output;
        if(nums.empty()) return output;

        int start = nums[0];
        int end = nums[0];
        for(int i = 1; i<nums.size(); i++){
            if(nums[i] == end + 1){
                end = nums[i];
            }
            else{
                if(start == end){
                    output.push_back(to_string(start));
                }
                else{
                    output.push_back(to_string(start) + "->" + to_string(end));
                }
                start = nums[i];
                end = nums[i];
            }
        }
        if(start == end){
            output.push_back(to_string(start));
        }
        else{
            output.push_back(to_string(start) + "->" + to_string(end));
        }
        return output;
    }
};
