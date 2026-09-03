class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        lastStart, lastEnd = result[-1]

        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]
            if currStart <= lastEnd:
                result[-1] = [min(lastStart, currStart), max(lastEnd, currEnd)]
            else:
                result.append([currStart, currEnd])
            lastStart, lastEnd = result[-1]
        
        return result
