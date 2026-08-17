class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 0 = unknown, -1 = no, 1 = yes
        isSafe = [0] * len(graph)
        visited = set()

        for i in range(len(graph)):
            visited.add(i)
            self.checkTerminal(graph, i, isSafe, visited)
        
        result = []
        for i in range(len(isSafe)):
            if isSafe[i] == 1:
                result.append(i)
        
        return result
    

    def checkTerminal(self, graph: List[List[int]], node: int, isSafe: List[int], visited) -> None:
        if isSafe[node] != 0:
            return
        
        for neighbor in graph[node]:
            if neighbor in visited:
                if isSafe[neighbor] != 1:
                    isSafe[node] = -1
                    return
                else:
                    continue
            
            visited.add(neighbor)
            self.checkTerminal(graph, neighbor, isSafe, visited)

            if isSafe[neighbor] == -1:
                isSafe[node] = -1
                return
        
        isSafe[node] = 1
