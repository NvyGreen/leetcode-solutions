class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, time in times:
            graph[start].append((end, time))
        dists = [float('inf')] * n
        dists[k - 1] = 0

        queue = [(0, k)]
        visited = set()

        while len(queue) > 0:
            dist, node = heapq.heappop(queue)
            if node in visited or dists[node - 1] == float('inf') or dist != dists[node - 1]:
                continue
            visited.add(node)

            for end, time in graph[node]:
                dists[end - 1] = min(dists[end - 1], dists[node - 1] + time)
                if dists[end - 1] == dists[node - 1] + time:
                    heapq.heappush(queue, (dists[end - 1], end))
        
        return max(dists) if len(visited) == n else -1
