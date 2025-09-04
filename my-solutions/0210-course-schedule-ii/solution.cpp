class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        int V = numCourses;
        vector<vector<int>> adj(V);
        vector<int> inDegree(V);
        vector<int> res;

        // Build graph
        for (auto &e : prerequisites) {
            int u = e[0], v = e[1];
            adj[v].push_back(u); // to do u, must first do v
            inDegree[u]++;
        }

        queue<int> q;
        // Find all starting courses (in-degree 0)
        for (int i = 0; i < V; i++) {
            if (inDegree[i] == 0) q.push(i);
        }

        // BFS (Kahn’s Algorithm)
        while (!q.empty()) {
            int u = q.front();
            res.push_back(u);
            q.pop();

            for (auto &v : adj[u]) {
                inDegree[v]--;
                if (inDegree[v] == 0) q.push(v);
            }
        }

        return res.size() < V ? vector<int>{} : res;
    }
};
