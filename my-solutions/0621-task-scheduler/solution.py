class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = {}
        for task in tasks:
            mp[task] = mp.get(task, 0) + 1
        
        pq = []
        for task, freq in mp.items():
            heapq.heappush_max(pq, (freq, task))
        
        q = []
        time = 1

        while len(pq) > 0:
            curr_task = heapq.heappop_max(pq)
            new_freq = curr_task[0] - 1
            if new_freq > 0:
                q.append((time + n + 1, new_freq, curr_task[1]))
            
            if len(pq) == 0 and q:
                time = q[0][0]
            elif len(pq) > 0:
                time += 1
            
            if q and time == q[0][0]:
                _, freq, task = q.pop(0)
                heapq.heappush_max(pq, (freq, task))
        
        return time
