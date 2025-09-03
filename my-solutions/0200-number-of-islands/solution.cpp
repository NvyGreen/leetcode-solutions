class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int check[4][2]={{0,1},{1,0},{-1,0},{0,-1}};
        int n = grid.size();int m = grid[0].size();
        vector<vector<int>> vis(n+1,vector<int>(m+1,0));
        int ans=0;
        for(int i =0; i< n ; i++){
            for(int j = 0 ; j< m ; j++){
                if(grid[i][j]=='1' && vis[i][j]==0){
                    ans++;
                    // cout<<i<<j<<" ";
                    queue<vector<int>> q;
                    q.push({i,j});
                    vis[i][j]=1;
                    while(!q.empty()){
                        vector<int> v = q.front();q.pop();
                        int a,b;a=v[0];b=v[1]; 
                        for(int k =0; k<4 ;k++){
                            int c =a+check[k][0];int d=b+check[k][1];
                            cout<<a<<b<<" ";
                            if(c>=0 && c<n && d>=0 && d<m && grid[c][d]=='1' && vis[c][d]==0){
                                q.push({c,d});vis[c][d]=1;
                            }
                        }
                    }
                }
            }
        }
        return ans;
    }
};
