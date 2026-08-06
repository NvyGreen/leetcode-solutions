class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tripQueue = []
        for trip in trips:
            numPassengers, start, end = trip
            heapq.heappush(tripQueue, (start, end, numPassengers))
        
        dropoff = []
        passengers = 0
        while len(tripQueue) > 0:
            start, end, numPassengers = heapq.heappop(tripQueue)
            while len(dropoff) > 0 and start >= dropoff[0][0]:
                _, dropPassengers = heapq.heappop(dropoff)
                passengers -= dropPassengers
            
            if passengers + numPassengers > capacity:
                return False
            heapq.heappush(dropoff, (end, numPassengers))
            passengers += numPassengers
        
        return True
