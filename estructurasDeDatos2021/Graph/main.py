from graphviz import Digraph
from graph import Graph

dot = Digraph(comment='Ejemplo de graficación')
print(" ***** Graph Creation Example ***** \n")
G = Graph()
# print(type(G))
G.add_node("A")
G.add_node("B")
G.add_node("C")
# print(G)
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "C")
print(G)


print(" ***** Graph Creation ***** \n")
G2 = Graph()

nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
edges = [("A", "C"), 
         ("B", "C"), 
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
  G2.add_node(node)
  dot.node(node,node)

for edge in edges:
  G2.add_edge(edge[0], edge[1])
  dot.edge(edge[0],edge[1])

print(G2)
print(dot.source)

print(" ***** Graph Simple Algorithm ***** \n")
dot.render('test-output/round-table.gv', view=True) 


