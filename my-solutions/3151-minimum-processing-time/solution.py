class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        maxTime = 0

        for i in range(len(processorTime)):
            start = i * 4
            maxTime = max(maxTime, processorTime[i] + max(tasks[start:start+4]))
        
        return maxTime
