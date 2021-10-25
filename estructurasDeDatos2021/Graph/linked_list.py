class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __repr__(self):
    return "Data: " + self.data


class LinkedList:
  def __init__(self):
    self.head = None

  def __repr__(self):
    node = self.head
    nodes = []
    while node is not None:
        nodes.append(node.data)
        node = node.next
    nodes.append("None")
    return " --> ".join(nodes)

  def traverse(self):
    node = self.head
    while node is not None:
        print(node.data)
        node = node.next

  def __iter__(self):
    node = self.head
    while node is not None:
        yield node
        node = node.next

  def insert_first(self, node):
    node.next = self.head
    self.head = node

  def insert_last(self, node):
    if self.head is None:
        self.head = node
    else:
        for current_node in self:
            pass
        current_node.next = node

  def remove(self, node_data):
    if self.head is None:
      raise Exception("La lista esta vacia")

    if self.head.data == node_data:
      self.head = self.head.next
      return

    previous_node = self.head

    for node in self:
      if node.data == node_data:
        previous_node.next = node.next
        return

      previous_node = node

    raise Exception("Nodo no existe en la lista")

  def insert_before(self, node_data, new_node):
    if self.head is None:
      raise Exception("La lista esta vacia")

    if self.head.data == node_data:
      return self.insert_first(new_node)

    previous_node = self.head

    for node in self:
      if node_data == node.data:
        previous_node.next = new_node
        new_node.next = node
        return

      previous_node = node

    raise Exception("Nodo objetivo no existe en la lista")

  def insert_after(self, node_data, new_node):
    if self.head is None:
      raise Exception("La lista esta vacia")

    for node in self:
      if node_data == node.data:
        new_node.next = node.next
        node.next = new_node
        return

    raise Exception("Nodo objetivo no existe en la lista")

  def reverse(self):
    if self.head is None:
        raise Exception("La lista esta vacia")

    prev = None
    node = self.head
    while node is not None:
      next = node.next
      node.next = prev
      prev = node
      node = next
    self.head = prev

