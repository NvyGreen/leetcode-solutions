class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        maxTime = 0

        for i in range(len(processorTime)):
            time = processorTime[i] + max(tasks[i * 4: i * 4 + 4])
            maxTime = max(maxTime, time)
        
        return maxTime
