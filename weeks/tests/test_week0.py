import unittest
 
from weeks.week0 import quickfind
from weeks.week0 import unionfindbase

class TestWeek0(unittest.TestCase):
    def test_QuickFind_ctr(self):
        expected = quickfind.QuickFind(10)
        self.assertIsNotNone(expected)

    def test_quickfind_withdata(self):
        data = [[4,3],[3,8],[6,5],[9,4],[2,1],[8,9]
             ,[5,0],[7,2],[6,1],[1,0],[6,7]]
        n = 10
        qf = quickfind.QuickFind(n)
        for p,q in data:
            qf.union(p,q)
        print(qf.__str__())
    
    
    

