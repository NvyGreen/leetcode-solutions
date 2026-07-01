"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        pq = []
        for employee in schedule:
            for timeslot in employee:
                heapq.heappush(pq, (timeslot.start, timeslot.end))
        
        result = []
        workStart, workEnd = heapq.heappop(pq)

        while pq:
            employeeStart, employeeEnd = heapq.heappop(pq)

            if employeeStart > workEnd:
                result.append(Interval(workEnd, employeeStart))
                workStart = employeeStart
                workEnd = employeeEnd
            else:
                workStart = min(workStart, employeeStart)
                workEnd = max(workEnd, employeeEnd)
        
        return result
        
