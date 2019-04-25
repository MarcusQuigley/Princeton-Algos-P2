import unittest

#from weeks import week2
from weeks.week2 import kruskal
from weeks.week2 import prims
from weeks.week2 import dijkstra

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
    self.assertEqual(expected, 1.81)
  
  def test_prims_compute_mst2(self): 
    prim = prims.Prims(5,self.create_graph2())
    expected  = prim.compute_mst()
    print(expected)
    self.assertEqual(expected,16)

  def test_dijkstra_exists(self):
    graph = self.create_edge_list()
    dijk = dijkstra.Dijkstra(6, graph)
    self.assertIsNotNone(dijk)

  def test_dijkstra_compute_sp(self):
    graph = self.create_edge_list()
    dijk = dijkstra.Dijkstra(6, graph)
    dijk.compute_shortestPath_withEdge_lists()
    self.assertEqual(len(dijk.arr_visited), 0)

  def test_dijkstra_compute_sp2(self):
    graph = self.create_edge_list2()
    dijk = dijkstra.Dijkstra(8, graph)
    dijk.compute_shortestPath_withEdge_lists()
    self.assertEqual(len(dijk.arr_visited), 0)

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

  def create_edge_list(self):
 
    graph = [[] for _ in range(6)]
    graph[0].append(list((1,5))) 
    graph[0].append(list((4,2)))
    graph[0].append(list((3,9)))

    graph[1].append(list((0,5))) 
    graph[1].append(list((2,2)))
    graph[2].append(list((1,2)))
    graph[2].append(list((3,3)))
    graph[3].append(list((2,3)))
    graph[3].append(list((0,9)))
    graph[3].append(list((5,2)))

    graph[4].append(list((0,2))) 
    graph[4].append(list((5,3)))
    graph[5].append(list((3,2)))
    graph[5].append(list((4,3)))
    return graph


  def create_edge_list2(self):
    graph = [[] for _ in range(8)]
    graph[0].append(list((1,5)))
    graph[0].append(list((7,8)))
    graph[0].append(list((4,9)))

    graph[1].append(list((3,15)))
    graph[1].append(list((7,4)))
    graph[1].append(list((2,12)))
    graph[2].append(list((3,3)))
    graph[2].append(list((6,11)))
    graph[3].append(list((6,9)))
    graph[4].append(list((7,5)))
    graph[4].append(list((5,4)))
    graph[4].append(list((6,20)))
    graph[5].append(list((2,1)))
    graph[5].append(list((6,13)))
    graph[7].append(list((2,7)))
    graph[7].append(list((5,6)))
    return graph

  def create_adjacency_list(self, n):
    graph = [[] for _ in range(n)]
    graph[0].append([0.16,7])
    graph[0].append([0.26,2])
    graph[0].append([0.38,4])
    graph[0].append([0.58,6])

    graph[1].append([0.32,5])
    graph[1].append([0.36,2])
    graph[1].append([0.29,3])
    graph[1].append([0.19,7])

    graph[2].append([0.36,1])
    graph[2].append([0.17,3])
    graph[2].append([0.26,0])
    graph[2].append([0.40,6])
    graph[2].append([0.34,7])

    graph[3].append([0.29,1])
    graph[3].append([0.17,2])
    graph[3].append([0.52,6])
 
    graph[4].append([0.35,5])
    graph[4].append([0.93,6])
    graph[4].append([0.38,0])
    graph[4].append([0.37,7])

    graph[5].append([0.32,1])
    graph[5].append([0.35,4])
    graph[5].append([0.28,7])

    graph[6].append([0.58,0])
    graph[6].append([0.40,2])
    graph[6].append([0.52,3])
    graph[6].append([0.93,4])

    graph[7].append([0.16,0])
    graph[7].append([0.28,5])
    graph[7].append([0.37,4])
    graph[7].append([0.19,1])
    graph[2].append([0.34,2])

    return graph


