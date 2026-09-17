class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        dists = defaultdict(list)
        self.bfs(x, adj, dists)
        self.bfs(y, adj, dists)
        self.bfs(z, adj, dists)

        count = 0
        for node, arr in dists.items():
            a, b, c = sorted(arr)
            if a ** 2 + b ** 2 == c ** 2:
                count += 1
        
        return count
    

    def bfs(self, root: int, adj: dict, dists: dict) -> None:
        queue = deque([(root, 0)])
        visited = set()

        while len(queue) > 0:
            node, dist = queue.popleft()
            visited.add(node)
            dists[node].append(dist)
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    queue.append((neighbor, dist + 1))
