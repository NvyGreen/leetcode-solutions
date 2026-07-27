class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x, y in points:
            distance = (x * x) + (y * y)
            heapq.heappush(pq, (distance, x, y))
        
        result = []
        while len(result) < k:
            _, x, y = heapq.heappop(pq)
            result.append([x, y])
        
        return result
