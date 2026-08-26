class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = 0
        heap = []

        for start, end in intervals:
            while len(heap) > 0 and heap[0] <= start:
                heapq.heappop(heap)
            if len(heap) == rooms:
                rooms += 1
            heapq.heappush(heap, end)
        
        return rooms
