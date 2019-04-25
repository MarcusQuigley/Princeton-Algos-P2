import sys

class Dijkstra(object):
    def __init__(self, n, graph):
        self.arr_distances = [sys.maxsize] * n
        self.arr_visited = list(range(n))# [for i in range(i)]
        self.arr_paths = [sys.maxsize] * n
        self.n = n
        self.graph = graph
        self.arr_distances[0]=0

    #gets the lowest value in arr_Distances of vertex thats not yet visited
    def _min_value(self):
        min = sys.maxsize
        index = 0
        for idx, item in enumerate(self.arr_distances):
            if idx in self.arr_visited:
                if item < min:
                    min = item
                    index = idx
        return index

    def compute_shortestPath_withEdge_lists(self):
  
        while len(self.arr_visited) > 0:
            vertex = self._min_value()
            if vertex in self.arr_visited:
                vertex_length = self.arr_distances[vertex]
                connected_vertices = self.get_connected_vertices(vertex)
                # for cv in connected_vertices:
                #     if cv[1] + vertex_length < self.arr_distances[cv[0]]:
                #         self.arr_distances[cv[0]] = cv[1] + vertex_length
                #         self.arr_paths[cv[0]] = vertex
                for v,weight in connected_vertices:
                    if weight + vertex_length < self.arr_distances[v]:
                        self.arr_distances[v] = weight + vertex_length
                        self.arr_paths[v] = vertex
                
                self.arr_visited.remove(vertex)
        return
    
    def get_connected_vertices(self, vertex):
        if vertex <=len(self.graph):
            return self.graph[vertex]
        return []


        