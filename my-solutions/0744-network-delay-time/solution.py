class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        queue = []
        minDists = []
        for i in range(n):
            if i + 1 == k:
                heapq.heappush(queue, (0, i + 1))
                minDists.append(0)
            else:
                heapq.heappush(queue, (float('inf'), i + 1))
                minDists.append(float('inf'))
        
        visited = set()
        while len(queue) > 0:
            dist, node = heapq.heappop(queue)
            if dist != minDists[node - 1]:
                continue
            
            for time in times:
                if time[0] == node and time[1] not in visited and minDists[time[1] - 1] > minDists[node - 1] + time[2]:
                    newTime = minDists[node - 1] + time[2]
                    minDists[time[1] - 1] = newTime
                    heapq.heappush(queue, (newTime, time[1]))
            
            visited.add(node)
        
        result = max(minDists)
        return result if result != float('inf') else -1
