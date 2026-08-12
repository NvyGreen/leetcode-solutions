class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            indegree[course] += 1
            adjList[prereq].append(course)
        
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        order = []
        while len(queue) > 0:
            course = queue.popleft()
            for nextCourse in adjList[course]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)
            order.append(course)
        
        return order if len(order) == numCourses else []
