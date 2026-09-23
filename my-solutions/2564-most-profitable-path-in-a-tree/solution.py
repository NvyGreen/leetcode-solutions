class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        n = len(amount)
        maxIncome = float('-inf')
        adj = [[] for _ in range(n)]
        bobPath = {}
        visited = [False] * n
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def findBobPath(node, time):
            bobPath[node] = time
            visited[node] = True

            if node == 0:
                return True
            
            for neighbor in adj[node]:
                if not visited[neighbor] and findBobPath(neighbor, time + 1):
                    return True
            
            bobPath.pop(node, None)
            return False
        
        findBobPath(bob, 0)

        visited = [False] * n
        queue = deque([(0, 0, 0)])

        while len(queue) > 0:
            source, time, income = queue.popleft()

            if source not in bobPath or bobPath[source] > time:
                income += amount[source]
            elif bobPath[source] == time:
                    income += (amount[source] // 2)
            
            if len(adj[source]) == 1 and source != 0:
                maxIncome = max(maxIncome, income)
            
            for neighbor in adj[source]:
                if not visited[neighbor]:
                    queue.append((neighbor, time + 1, income))
            visited[source] = True
        
        return maxIncome
