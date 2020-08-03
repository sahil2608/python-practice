class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head # it will point towards the old self.head
        self.head = node # adding the value

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head: # checking if list is not empty
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node) # Using new node method if the element we want to insert is at starting

        perv_node = self.head # to keep track of last checked node
        for node in self: # traversing the list
            if node.data == target_node_data:
                perv_node.next = new_node
                new_node.next = node
                return
            perv_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data: # check if the node to be removed is the current head of the list
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


llist = LinkedList()

first_node = Node("a")
llist.head = first_node

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)

llist = LinkedList(["a", "b", "c", "d"])
llist.add_first(Node("z"))
llist.add_last(Node("e"))
llist.add_after("c", Node("cc"))
llist.add_before("c", Node("bb"))
# llist.add_after("f", Node("cc")) # this will throw exception because it does not exist
print(llist)