class Solution {
public:
    void dfs(unordered_map<string, vector<pair<string, double>>>&mpp, string src, string dest, double & ans, double product, unordered_set<string>&visited){
        if(visited.find(src) != visited.end() || visited.find(dest) != visited.end()){
            return;
        }
        visited.insert(src);
        if(src == dest){
            ans = product;
            return;
        }
        for(auto & p: mpp[src]){
            string v = p.first;
            double val = p.second;

            dfs(mpp, v, dest, ans, product * val, visited);
        }

    }
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        int n = equations.size();
        unordered_map<string, vector<pair<string, double>>>mpp;
        
        for(int i = 0; i<n; i++){
            string u = equations[i][0];
            string v = equations[i][1];

            double val = values[i];
            mpp[u].push_back({v, val});
            mpp[v].push_back({u, 1.0/val});
        }

        vector<double>result;
        for(auto &query: queries){
            string src = query[0];
            string dest = query[1];

            double ans = -1.0;
            double product = 1.0;
            if(mpp.find(src) == mpp.end() || mpp.find(dest) == mpp.end()){
                result.push_back(ans);
                continue;
            }
            else{
                unordered_set<string>visited;

                dfs(mpp, src, dest, ans, product, visited);

            }
            result.push_back(ans);
        }

        return result;
        
    }
};
