class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        return max(self.dfs(graph, 0, -1, hasApple) - 2, 0)
    

    def dfs(self, graph, node: int, parent: int, hasApple: list[bool]) -> int:
        paths = 0
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            paths += self.dfs(graph, neighbor, node, hasApple)
        
        if paths > 0:
            return paths + 2
        return 2 if hasApple[node] else 0
