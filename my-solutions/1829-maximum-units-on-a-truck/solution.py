class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        load, units, index = 0, 0, 0

        while index < len(boxTypes) and load < truckSize:
            count, weight = boxTypes[index]
            print(load + count)
            if load + count > truckSize:
                count -= load + count - truckSize
            print(count, weight)
            
            load += count
            units += count * weight
            index += 1
        
        return units
