class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        edges = defaultdict(list)
        indgr = [0] * numCourses

        for course, prereq in prerequisites:
            indgr[course] += 1
            edges[prereq].append(course)
        
        queue = deque([])
        for i in range(numCourses):
            if indgr[i] == 0:
                queue.append(i)
        schedule = set()

        while len(queue) > 0:
            taken = queue.popleft()
            for course in edges[taken]:
                indgr[course] -= 1
                if indgr[course] == 0:
                    queue.append(course)
            schedule.add(taken)
        
        return len(schedule) == numCourses
