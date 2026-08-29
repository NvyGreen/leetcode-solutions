class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        totalCount, totalUnits = 0, 0

        for i in range(len(boxTypes)):
            count, units = boxTypes[i]
            if totalCount + count > truckSize:
                count -= count + totalCount - truckSize
            
            totalCount += count
            totalUnits += count * units
            if totalCount >= truckSize:
                break
        
        return totalUnits
