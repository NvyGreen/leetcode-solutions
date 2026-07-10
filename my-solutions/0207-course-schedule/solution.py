class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = []
        for i in range(numCourses):
            adj_list.append([])
        
        for course, prereq in prerequisites:
            indegree[course] += 1
            adj_list[prereq].append(course)
        
        queue = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        top_list = []
        while len(queue) > 0:
            node = queue.popleft()
            for course in adj_list[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
            
            top_list.append(node)
        
        return len(top_list) == numCourses
