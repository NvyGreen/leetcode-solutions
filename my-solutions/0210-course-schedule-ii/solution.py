class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            edges[prereq].append(course)
            indegree[course] += 1
        
        queue = deque([])
        order = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while len(queue) > 0:
            course = queue.popleft()
            if edges.get(course) is not None:
                for newCourse in edges[course]:
                    indegree[newCourse] -= 1
                    if indegree[newCourse] == 0:
                        queue.append(newCourse)
            order.append(course)
        
        if len(order) != numCourses:
            return []
        return order
