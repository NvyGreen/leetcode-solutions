class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        start, end = 0, len(intervals)
        newStart, newEnd = newInterval
        while start < end:
            mid = (start + end) // 2
            if intervals[mid][1] < newStart:
                start = mid + 1
            else:
                end = mid
        left = start
        
        start, end = 0, len(intervals)
        while start < end:
            mid = (start + end) // 2
            if intervals[mid][0] > newEnd:
                end = mid
            else:
                start = mid + 1
        right = start - 1

        result = intervals[:left]

        if left > right:
            result.append([newStart, newEnd])
        else:
            mergedStart = min(newStart, intervals[left][0])
            mergedEnd = max(newEnd, intervals[right][1])
            result.append([mergedStart, mergedEnd])
        
        result += intervals[right + 1:]
        return result
