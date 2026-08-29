class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = defaultdict(int)
        for task in tasks:
            task_freq[task] -= 1
        
        ready = []
        for task, freq in task_freq.items():
            heapq.heappush(ready, (freq, task))
        
        cooldown = []
        time = 0
        while len(ready) > 0:
            freq, task = heapq.heappop(ready)
            freq += 1
            if freq < 0:
                heapq.heappush(cooldown, (time + n + 1, freq, task))
            
            time += 1
            if len(ready) == 0 and len(cooldown) > 0 and cooldown[0][0] > time:
                time = cooldown[0][0]
            
            while len(cooldown) > 0 and cooldown[0][0] <= time:
                _, freq, task = heapq.heappop(cooldown)
                heapq.heappush(ready, (freq, task))
        
        return time
