class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        lastStart = result[0][0]
        lastEnd = result[0][1]
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]
            if currStart <= lastEnd:
                result[-1][1] = max(currEnd, lastEnd)
                lastEnd = result[-1][1]
            else:
                result.append(intervals[i])
                lastStart, lastEnd = result[-1]

        return result
