class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        lastStart, lastEnd = intervals[0]
        rm = 0

        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]
            if currStart < lastEnd:
                rm += 1
                lastEnd = min(lastEnd, currEnd)
            else:
                lastStart, lastEnd = currStart, currEnd
        
        return rm
