class Vertex:
    def __init__(self, vertexId: int = None):
        self.vertexId = vertexId
        self.offline = False
        self.powerGridId = -1



class Graph:
    def __init__(self):
        self.adj = {}
        self.vertices = {}
    

    def addVertex(self, vertexId: int, value: Vertex):
        self.vertices[vertexId] = value
        self.adj[vertexId] = []
    

    def addEdge(self, u: int, v: int):
        self.adj[u].append(v)
        self.adj[v].append(u)
    

    def getVertexValue(self, vertexId: int) -> Vertex:
        return self.vertices[vertexId]
    

    def getConnectedVertices(self, vertexId: int) -> List[int]:
        return self.adj[vertexId]



class Solution:
    def traverse(self, u, powerGridId: int, powerGrid: List[int], graph) -> None:
        u.powerGridId = powerGridId
        heapq.heappush(powerGrid, u.vertexId)
        for vid in graph.getConnectedVertices(u.vertexId):
            v = graph.getVertexValue(vid)
            if v.powerGridId == -1:
                self.traverse(v, powerGridId, powerGrid, graph)


    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = Graph()
        for i in range(c):
            v = Vertex(i + 1)
            graph.addVertex(i + 1, v)
        
        for u, v in connections:
            graph.addEdge(u, v)
        
        powerGrids = []
        powerGridId = 0

        for i in range(1, c + 1):
            v = graph.getVertexValue(i)
            if v.powerGridId == -1:
                powerGrid = []
                self.traverse(v, powerGridId, powerGrid, graph)
                powerGrids.append(powerGrid)
                powerGridId += 1
        
        ans = []
        for q in queries:
            op, x = q
            if op == 1:
                vertex = graph.getVertexValue(x)
                if not vertex.offline:
                    ans.append(x)
                else:
                    powerGrid = powerGrids[vertex.powerGridId]
                    while powerGrid and graph.getVertexValue(powerGrid[0]).offline:
                        heapq.heappop(powerGrid)
                    ans.append(powerGrid[0] if powerGrid else -1)
            else:
                graph.getVertexValue(x).offline = True
        
        return ans
        
