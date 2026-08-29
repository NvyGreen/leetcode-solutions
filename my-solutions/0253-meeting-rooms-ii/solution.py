class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = 0
        queue = []

        for start, end in intervals:
            while len(queue) > 0 and start >= queue[0]:
                heapq.heappop(queue)
            
            if len(queue) == rooms:
                rooms += 1
            
            heapq.heappush(queue, end)
        
        return rooms
