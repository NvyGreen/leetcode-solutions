class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        remove = 0
        lastStart, lastEnd = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] < lastEnd:
                remove += 1
                if intervals[i][1] < lastEnd:
                    lastStart, lastEnd = intervals[i]
            else:
                lastStart, lastEnd = intervals[i]
        
        return remove
