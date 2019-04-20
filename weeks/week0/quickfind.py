from .unionfindbase import UnionFindBase

class QuickFind(UnionFindBase):
    def __init__(self, n):
        super().__init__(n)
        print('created QuickFind')

    def union(self, p,q):
        pid = self._id[p]
        qid = self._id[q]

        if qid == pid: return
        
        for i in range(len(self._id)):
            if self._id[i] == pid:
                self._id[i] = qid
        self._num_components -= 1

    def find(self,i):
        return self._id[i]