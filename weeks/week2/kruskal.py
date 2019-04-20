
from queue import PriorityQueue
class Kruskal(object):
    def __init__(self, n, graph):
        self._n = n
        self._quickfind = self.QuickFind(n)
        self._queue = PriorityQueue(len(graph))
        self._populate_queue(self._queue, graph)
 
    def _populate_queue(self,queue, graph):
        for item in graph:
            self._queue.put(item)
    
    def compute_mst(self):
        results = []
        counter = self._n-1
        while counter > 0:
            edge = self._queue.get()
            if self._quickfind.union(edge[1], edge[2]):
                results.append(edge)
                counter -= 1
        return results

    class QuickFind(object):
        def __init__(self, n):
            self._ids = [i for i in range(n)]
        
        def union(self, p,q):
            pid = self.find(p)
            qid = self.find(q)
            if pid == qid: return False
            
            for idx, item in enumerate(self._ids):
                if item == pid:
                    self._ids[idx] = qid
            return True

        def find(self, v):
            return self._ids[v]

    
    def __str__(self):
        return 'Kruskal impl'
                