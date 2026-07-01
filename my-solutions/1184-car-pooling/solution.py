class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        remainingTrips = []
        for trip in trips:
            tripPassengers, startLoc, endLoc = trip
            heapq.heappush(remainingTrips, (startLoc, endLoc, tripPassengers))
        
        numPassengers = 0
        currLoc = 0
        currTrips = []

        while remainingTrips:
            if not currTrips:
                nextStart, nextEnd, nextPassengers = heapq.heappop(remainingTrips)
                currLoc = nextStart
                numPassengers += nextPassengers
                if numPassengers > capacity:
                    return False
                heapq.heappush(currTrips, (nextEnd, nextPassengers))
            
            if not remainingTrips:
                return True

            currLoc = min(currTrips[0][0], remainingTrips[0][0])
            while currTrips and currLoc == currTrips[0][0]:
                _, oldPassengers = heapq.heappop(currTrips)
                numPassengers -= oldPassengers
            
            while remainingTrips and currLoc == remainingTrips[0][0]:
                _, nextEnd, nextPassengers = heapq.heappop(remainingTrips)
                numPassengers += nextPassengers
                if numPassengers > capacity:
                    return False
                heapq.heappush(currTrips, (nextEnd, nextPassengers))
        
        return True
        
