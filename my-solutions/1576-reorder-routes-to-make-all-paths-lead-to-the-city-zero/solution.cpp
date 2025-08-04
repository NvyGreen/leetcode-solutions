class Solution {
public:
   map<pair<int,int>,bool>mp;
   int ans = 0;
    void dfs(int node,vector<vector<int>>&adj,int parent){
        for(int j = 0; j< adj[node].size();j++){
            int neigh = adj[node][j];
            if(neigh == parent) continue;
            if(mp.find({node,neigh}) != mp.end())
            ans ++;
                dfs(neigh,adj,node);
            
        }
        
    }
    int minReorder(int n, vector<vector<int>>& connections) {
        
        int m = connections.size();
        vector<vector<int>>adj(n);
        for(int i = 0; i< m;i++){
            int u = connections[i][0];
            int v = connections[i][1];
            adj[u].push_back(v);
            adj[v].push_back(u);
            mp[{u,v}] =1;
        }
        dfs(0,adj,-1);
        return ans;

    }
};
