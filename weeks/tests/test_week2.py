import unittest

#from weeks import week2
from weeks.week2 import kruskal

class Kruskal_Tests(unittest.TestCase):
  def test_kruskal_ctr(self): 
    expected = kruskal.Kruskal(8,self.create_graph())
    self.assertIsNotNone(expected)

  def test_kruskal_compute_mst(self): 
    krusk = kruskal.Kruskal(8,self.create_graph())
    expected = krusk.compute_mst()
    print(expected)
    self.assertIsNotNone(expected)

  def create_graph(self):
    graph = []
    graph.append((0.16,0,7))
    graph.append((0.17,2,3))
    graph.append((0.19,1,7))
    graph.append((0.26,0,2))
    graph.append((0.28,5,7))
    graph.append((0.29,1,3))
    graph.append((0.32,1,5))
    graph.append((0.34,2,7))
    graph.append((0.35,4,5))
    graph.append((0.36,1,2))
    graph.append((0.37,4,7))
    graph.append((0.38,0,4))
    graph.append((0.4,6,2))
    graph.append((0.52,3,6))
    graph.append((0.58,6,0))
    graph.append((0.93,6,4))

    return graph


   