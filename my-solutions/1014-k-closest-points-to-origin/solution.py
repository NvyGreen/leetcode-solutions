class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for x, y in points:
            dist = math.sqrt(x*x + y*y)
            heapq.heappush(pq, (dist, x, y))
        
        result = []
        for i in range(k):
            _, x, y = heapq.heappop(pq)
            result.append([x, y])
        
        return result
        
