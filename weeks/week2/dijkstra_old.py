import sys

class DijkstraOLD(object):
    def __init__(self, vertices):
        self._vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        
    #gets the min distance from the set of vertices not yet touched
    def _min_distance(self, distance, remaining_vertices):
        min = sys.maxsize
        for v in range(self._vertices):
            if distance[v] < min and remaining_vertices[v] == False:
                min = distance[v]
                min_index = v
        
        return min_index
    
    def compute_dijkstra(self, start_vertex):
        distance = [sys.maxsize] * self._vertices
        distance[start_vertex] = 0
        remaining_vertices = [False] * self._vertices

        for vertex in range(self._vertices):
            min_dist_vertex = self._min_distance(distance,remaining_vertices)
            remaining_vertices[vertex] = True
            for v in range(self._vertices):
                if self.graph[min_dist_vertex][v] > 0 \
                     and remaining_vertices[v] == False \
                     and distance[v] > (distance[min_dist_vertex] + self.graph[min_dist_vertex][v]):
                    distance[v] = (distance[min_dist_vertex] + self.graph[min_dist_vertex][v])



g = DijkstraOLD(5) 
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
#            [4, 0, 8, 0, 0, 0, 0, 11, 0], 
#            [0, 8, 0, 7, 0, 4, 0, 0, 2], 
#            [0, 0, 7, 0, 9, 14, 0, 0, 0], 
#            [0, 0, 0, 9, 0, 10, 0, 0, 0], 
#            [0, 0, 4, 14, 10, 0, 2, 0, 0], 
#            [0, 0, 0, 0, 0, 2, 0, 1, 6], 
#            [8, 11, 0, 0, 0, 0, 1, 0, 7], 
#            [0, 0, 2, 0, 0, 0, 6, 7, 0]   ]

g.graph = [ [0,3,0,5,0],
            [3,0,7,0,0],
            [0,7,0,0,1],
            [5,0,0,0,9],
            [0,0,1,9,0]]
  
g.compute_dijkstra(0)