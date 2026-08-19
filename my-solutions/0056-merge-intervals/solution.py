class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        lastStart, lastEnd = result[0]

        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]
            if currStart >= lastStart and currStart <= lastEnd:
                result[-1][1] = max(currEnd, lastEnd)
            else:
                result.append(intervals[i])
            lastStart, lastEnd = result[-1]
        
        return result
