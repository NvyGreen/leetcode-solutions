class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        i = 0
        while i < len(gas):
            if gas[i] < cost[i]:
                i += 1
                continue
            
            canFinish, nextIndex = self.startTrip(gas, cost, i)
            if canFinish:
                return i
            i = nextIndex
        
        return -1
    

    def startTrip(self, gas: List[int], cost: List[int], start: int) -> (bool, int):
        tank = gas[start]
        curr = start

        while tank >= cost[curr]:
            tank -= cost[curr]
            curr = (curr + 1) % len(gas)
            if curr == start:
                return True, curr
            tank += gas[curr]
        
        return False, curr
