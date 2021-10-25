import unittest
from graph import Graph


class TestGraph(unittest.TestCase):

    def test_path(self):

      G = Graph()

      nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
      edges = [("A", "C"), 
              ("B", "C"), 
              ("B", "D"),
              ("B", "D"),
              ("B", "H"),
              ("C", "B"),
              ("C", "E"),
              ("D", "A"),
              ("D", "G"),
              ("E", "H"),
              ("E", "B"),
              ("F", "E"),
              ("G", "B"),
              ("G", "F")
              ]

      for node in nodes:
        G.add_node(node)

      for edge in edges:
        G.add_edge(edge[0], edge[1])

      self.assertEqual(G.path_exists("A", "H"), True, "True, a path exists")
      self.assertEqual(G.path_exists("E", "F"), True, "True, a path exists")
      self.assertEqual(G.path_exists("G", "A"), True, "True, a path exists")
      self.assertEqual(G.path_exists("H", "D"), True, "False, a path does not exist")


    def test_path_under_two(self):
      G2 = Graph()

      self.assertEqual(G2.path_under_2_moves("A", "B"), False, "Error msg")
      
if __name__ == '__main__':
    unittest.main()