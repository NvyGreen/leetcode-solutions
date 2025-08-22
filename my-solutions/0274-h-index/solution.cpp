class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        vector<int> freq(n + 1);

        for(int num : citations){
            if(num >= n) freq[n]++;
            else freq[num]++;
        }

        int idx = n;
        int sum = freq[n];

        while(sum < idx){
            idx--;
            sum += freq[idx];
        }
        return idx;
    }
};
