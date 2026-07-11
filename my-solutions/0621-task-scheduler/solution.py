class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = {}
        for task in tasks:
            task_freq[task] = task_freq.get(task, 0) + 1
        
        ready_q = []
        for task, freq in task_freq.items():
            task_tup = (-freq, task)
            heapq.heappush(ready_q, task_tup)
        
        time = 0
        cooldown_q = []
        while len(ready_q) > 0:
            curr_freq, task = heapq.heappop(ready_q)            
            curr_freq = -curr_freq
            curr_freq -= 1

            if curr_freq > 0:
                task_tup = (time + n + 1, -curr_freq, task)
                heapq.heappush(cooldown_q, task_tup)
            
            time += 1
            while len(cooldown_q) > 0 and cooldown_q[0][0] <= time:
                _, curr_freq, task = heapq.heappop(cooldown_q)
                task_tup = (curr_freq, task)
                heapq.heappush(ready_q, task_tup)
            
            if len(ready_q) == 0 and len(cooldown_q) > 0:
                time = cooldown_q[0][0]
                while len(cooldown_q) > 0 and cooldown_q[0][0] <= time:
                    _, curr_freq, task = heapq.heappop(cooldown_q)
                    task_tup = (curr_freq, task)
                    heapq.heappush(ready_q, task_tup)
        
        return time
        
