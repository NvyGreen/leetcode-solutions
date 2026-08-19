class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            indegree[course] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        coursesTaken = 0
        while len(queue) > 0:
            prereq = queue.popleft()
            for course in adjList[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
            coursesTaken += 1
        
        return coursesTaken == numCourses
