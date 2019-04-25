import unittest
from weeks.week2 import dijkstra
from weeks.week2 import bellman_ford

class TestWeek2ShortestPath(unittest.TestCase):

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

    def test_bellmanford_exists(self):
        graph = self.create_edge_list()
        bf = bellman_ford.BellmanFord(6, graph)
        self.assertIsNotNone(bf)

    def test_bellmanford_compute_sp(self):
        graph = self.create_edge_list()
        bf = bellman_ford.BellmanFord(6, graph)
        actual = bf.compute_shortestpath()
        self.assertIsNotNone(actual)
    
    #not workking for edgelist
    def test_bellmanford_compute_sp2(self):
        graph = self.create_edge_list4()
        bf = bellman_ford.BellmanFord(6, graph)
        actual = bf.compute_shortestpath2()
        self.assertIsNotNone(actual)


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
    
    def create_edge_list3(self):
        graph = [[] for _ in range(6)]
        graph[0].append(list((1,10)))
        graph[0].append(list((5,8)))
        graph[1].append(list((3,2)))
        graph[2].append(list((1,1)))

        graph[3].append(list((2,-2)))
        graph[4].append(list((3,-1)))
        graph[4].append(list((1,-4)))
        graph[5].append(list((4,1)))
        return graph

    def create_edge_list4(self):
        g = []
        g.append([0,1,10])
        g.append([0,5,8])
        g.append([1,3,2])
        g.append([2,1,1])
        g.append([3,2,-2])
        g.append([4,3,-1])
        g.append([4,1,-4])
        g.append([5,4,1])
       
        # g.append([0,1,10])
        # g.append([0,1,10])
        return g
