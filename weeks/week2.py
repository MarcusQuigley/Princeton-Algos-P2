import algohelpers.graph
import algohelpers.bag
import io
import numpy


from algohelpers.graph import Graph
from algohelpers.bag import Bag

def test_graph():
  graph = Graph(None,7)
  graph.add_edge(0,1)
  graph.add_edge(0,2)
  graph.add_edge(0,5)
  graph.add_edge(0,6)
  graph.add_edge(6,4)
  graph.add_edge(4,3)
  graph.add_edge(4,5)
  graph.add_edge(5,3)
  
  print(graph.__str__())

 

 