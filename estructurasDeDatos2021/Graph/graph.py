from linked_list import LinkedList, Node


class Graph:
  def __init__(self):
    self.adjacency_lists = []

  def __repr__(self):
    g = ""

    for element in self.adjacency_lists:
      g += element["node"] + " => " + str(element["adj_list"]) + "\n"

    return g

  def add_node(self, node_label):
    self.adjacency_lists.append({
                                "node": node_label,
                                "adj_list": LinkedList()
                                })

  def add_edge(self, start_node, end_node):
    for element in self.adjacency_lists: 
      if element["node"] == start_node:
        element["adj_list"].insert_first(Node(end_node))
        return

  def path_exists(self, start, end):
    return True

  def path_under_2_moves(self, start, end):
    return False


