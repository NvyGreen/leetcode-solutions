class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& inl) {
        int n=inl.size();
        for(int i=0;i<n;i++){
            swap(inl[i][0],inl[i][1]);
        }
        sort(inl.begin(),inl.end());
        int c=1;
        int l=inl[0][0];
        for(int i=1;i<n;i++){
            if(inl[i][1]>=l){
                l=inl[i][0];
                c++;
            }
        }
        return n-c;
    }
};
