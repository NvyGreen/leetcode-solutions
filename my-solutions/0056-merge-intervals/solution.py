class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        result = [sorted_intervals[0]]
        prev_start, prev_end = result[0]

        for i in range(1, len(sorted_intervals)):
            curr_start, curr_end = sorted_intervals[i]
            if curr_start <= prev_end:
                result[-1] = [prev_start, max(prev_end, curr_end)]
            else:
                result.append([curr_start, curr_end])
            
            prev_start, prev_end = result[-1]

        return result
        
