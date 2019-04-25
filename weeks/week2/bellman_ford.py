import sys

class BellmanFord(object):
    def __init__(self, n, graph):
        self.n = n
        self.graph = graph

    
    def compute_shortestpath(self):
        distances = [sys.maxsize] * self.n
        distances[0] = 0
        counter=0
        
        for i in range(self.n-1):
            for v1 in range(self.n):
                for v2, weight in self.graph[v1]:
                    # for v2, weight in self.graph[v1]:
                    measurement = distances[v1] + weight
                    if measurement < distances[v2]:
                        distances[v2] = measurement
                    counter +=1
        
        #check for cycle
        for v1 in range(self.n-1):
            for v2, weight in self.graph[v1]:
                measurement = distances[v1] + weight
                if measurement < distances[v2]:
                    print ('cycle exists')
                    return []
        return distances

    def compute_shortestpath2(self):
        distances = [sys.maxsize] * self.n
        distances[0] = 0
        counter=0
        
        for i in range(self.n-1):
            for v1, v2, weight in self.graph:
                measurement = distances[v1] + weight
                if measurement < distances[v2]:
                    distances[v2] = measurement
                counter +=1
        
        #check for cycle
        #for v1 in range(self.n-1):
        for v1, v2, weight in self.graph:
            measurement = distances[v1] + weight
            if measurement < distances[v2]:
                print ('cycle exists')
                return []
        return distances
            