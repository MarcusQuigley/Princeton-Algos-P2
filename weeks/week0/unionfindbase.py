
from abc import ABC, abstractmethod

class UnionFindBase(ABC):
    def __init__(self, n):
        self._num_components = n
        self._id = [i for i in range(n)]
        self._count = 0

    @abstractmethod
    def union(self, p, q):
        pass

    @abstractmethod            
    def find(self, i):
        pass

    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def count(self):
        return self._count
    
    def __str__(self):
        return str(self._id)

     