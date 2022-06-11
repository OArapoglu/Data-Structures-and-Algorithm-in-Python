"""
LINKED LIST OPERATIONS
    Create a node from Node including data and next properties.
    Create a linked list.
    Push a node into the head of a linked list.
    Append a node into a tail of linked list.
    Insert a node into a linked list.
    Remove a node from a linked list.
    Print nodes in a linked list.
"""


class Node:
    """A data structure to keep a data and next pointer."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    """Linked list to keep nodes in order."""

    def __init__(self):
        self.head = None

    def create_linked_list(self, node_ids: list):
        """Create a linked list from given ids."""
        if node_ids:
            nodes = []
            for data in node_ids:
                nodes.append(Node(data))
            self.head = nodes[0]
            if len(nodes) > 1:
                self.head.next = nodes[1]
                for i in range(1, len(nodes) - 1):
                    nodes[i].next = nodes[i + 1]

    def push_node(self, node_id: int):
        """Set a node as a head node of the linked list."""
        if isinstance(node_id, int):
            node = Node(node_id)
            node.next = self.head
            self.head = node
        else:
            print("Node id must be integer!")

    def append_node(self, node_id: int):
        """Set a node as a tail node of the linked list."""
        if isinstance(node_id, int):
            node = Node(node_id)
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = node
        else:
            print("Node id must be integer!")

    @staticmethod
    def insert_after_node(new_node_id: int, prev_node_id: Node):
        """Insert a middle node into the linked list."""
        if isinstance(new_node_id, int):
            node = Node(new_node_id)
            node.next = prev_node_id.next
            prev_node_id.next = node
        else:
            print("Node id must be integer!")

    def remove_node(self, node_id: int):
        """Remove a node from the linked list."""
        if isinstance(node_id, int) and self.head.data is not None:
            if self.head.data == node_id:
                if self.head.next is not None:
                    self.head = self.head.next
                else:
                    self.head = None
            else:
                current_node = self.head
                prev_node = self.head
                while current_node:
                    if current_node.data == node_id:
                        break
                    prev_node = current_node
                    current_node = current_node.next
                if current_node:
                    prev_node.next = current_node.next
        else:
            print("Node id must be integer!")

    def get_node(self, node_id: int) -> Node:
        """Get a node according to node id."""
        current_node = None
        if isinstance(node_id, int):
            current_node = self.head
            while current_node:
                if current_node.data == node_id:
                    return current_node
                current_node = current_node.next
        else:
            print("Node id must be integer!")
        return current_node

    def print_list(self):
        """Print current nodes in the linked list."""
        current = self.head
        while current is not None:
            print(f"Node {current}")
            current = current.next
        print("************************************")


def print_selection():
    """Selection list."""
    print("************************************")
    print(
        "1-Insert a list number to create a linked list.\n"
        "2-Push a node to make it head node of the linked list.\n"
        "3-Append a node to make it last node of linked list.\n"
        "4-Insert a node after a node in the linked list.\n"
        "5-Remove a node from the linked list.\n"
        "6-Print the nodes of your linked list.\n"
        "7-Exit.\n"
    )
    print("************************************")


def main():
    """Main program for linked list operations."""
    linked_list = None
    while True:
        try:
            print_selection()
            selection = input("Enter your selection:")
            if selection != "1" and linked_list is None:
                print("You must initially create a linked list!")
                continue
            if selection == "1":
                node_ids = [int(x) for x in input("Enter node ids:").split()]
                linked_list = LinkedList()
                linked_list.create_linked_list(node_ids)
            elif selection == "2":
                node_id = int(input("Enter node id:"))
                linked_list.push_node(node_id)
            elif selection == "3":
                node_id = int(input("Enter node id:"))
                linked_list.append_node(node_id)
            elif selection == "4":
                new_node_id = int(input("Enter new node id:"))
                prev_node_id = int(input("Enter previuos node id:"))
                prev_node = linked_list.get_node(prev_node_id)
                if prev_node:
                    linked_list.insert_after_node(new_node_id, prev_node)
                else:
                    print(f"There is no node with {prev_node_id} id.")
            elif selection == "5":
                node_id = int(input("Enter node id:"))
                linked_list.remove_node(node_id)
            elif selection == "6":
                linked_list.print_list()
            elif selection == "7":
                break
            else:
                print("The selection is invalid!")
        except ValueError:
            print("You must enter integer value for node id!")


if __name__ == "__main__":
    main()
