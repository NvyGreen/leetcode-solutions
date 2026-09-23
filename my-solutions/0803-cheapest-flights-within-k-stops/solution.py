class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(list)
        for start, end, price in flights:
            edges[start].append((end, price))
        
        dists = [float('inf')] * n
        dists[src] = 0
        queue = deque([])
        for end, price in edges[src]:
            queue.append((end, price, 1))
        
        while len(queue) > 0:
            city, price, stops = queue.popleft()
            if price < dists[city]:
                dists[city] = price
                if city != dst and stops <= k:
                    for end, cost in edges[city]:
                        queue.append((end, cost + price, stops + 1))
        
        return dists[dst] if dists[dst] != float('inf') else -1
