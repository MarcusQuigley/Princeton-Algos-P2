from queue import PriorityQueue

class Prims(object):
    def __init__(self, n, graph):
        self._n = n
        self._graph = graph
        self._pq =  PriorityQueue(len(graph))
    
    def compute_mst(self, graph = None):
        result = []
        counter = self._n - 1
        if graph is None: graph = self._graph
        self._pq = self._populatequeue(graph,[0,0])
        while counter > 0:
            edge = self._pq.get()
            result.append(edge[1])
            result.append( edge[2])
            counter -= 1
            self._pq =  self._populatequeue(graph,result)
        return result
    
    def _populatequeue(self, graph, tree_edges):
        pq = PriorityQueue()
        for edge in graph:
            if edge[1] in tree_edges and edge[2] in tree_edges:
                continue
            else:
               if edge[1] in tree_edges or edge[2] in tree_edges:
                   pq.put(edge)
        return pq

