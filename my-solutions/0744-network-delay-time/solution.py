class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[1], time[2]))
        dists = [float('inf')] * n
        dists[k - 1] = 0
        
        queue = [(0, k)]
        visited = set()
        while len(queue) > 0:
            dist, node = heapq.heappop(queue)
            if node in visited or dists[node - 1] != dist or dist == float('inf'):
                continue
            visited.add(node)

            for neighbor, weight in graph[node]:
                dists[neighbor - 1] = min(dists[neighbor - 1], dists[node - 1] + weight)
                if dists[neighbor - 1] == dists[node - 1] + weight:
                    heapq.heappush(queue, (dists[neighbor - 1], neighbor))
        
        return max(dists) if len(visited) == n else -1
