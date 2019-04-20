import unittest

#from weeks import week2
from weeks.week2 import kruskal
from weeks.week2 import prims

class TestWeek2(unittest.TestCase):
  def test_kruskal_ctr(self): 
    expected = kruskal.Kruskal(8,self.create_graph())
    self.assertIsNotNone(expected)

  def test_kruskal_compute_mst(self): 
    krusk = kruskal.Kruskal(8,self.create_graph())
    expected = krusk.compute_mst()
    print(expected)
    self.assertIsNotNone(expected)

  def test_prims_ctr(self): 
    expected = prims.Prims(8,self.create_graph())
    self.assertIsNotNone(expected)

  def test_prims_compute_mst(self): 
    prim = prims.Prims(8,self.create_graph())
    expected  = prim.compute_mst()
    print(expected)
    self.assertIsNotNone(expected)
  
  def test_prims_compute_mst2(self): 
    prim = prims.Prims(5,self.create_graph2())
    expected  = prim.compute_mst()
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

  def create_graph2(self):
    graph = []
    graph.append((2,0,1))
    graph.append((6,0,3))
    graph.append((2,1,0))
    graph.append((3,1,2))
    graph.append((8,1,3))
    graph.append((5,1,4))
    graph.append((3,2,1))
    graph.append((7,2,4))
    graph.append((6,3,0))
    graph.append((8,3,1))
    graph.append((9,3,4))
    graph.append((5,4,1))
    graph.append((7,4,2))
    graph.append((9,4,3))
 

    return graph


   