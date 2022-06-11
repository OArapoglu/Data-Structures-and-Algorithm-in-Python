"""
STACK OPERATIONS
    Create a node from Node including data and next properties.
    Push a node into the stack.
    Pop a node from the stack.
    Peek a node from the stack.
    IsEmpty to check whether the stack is empty or not
    Display nodes in a stack.
"""


class Node:
    """A data structure to keep a data and next pointer."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Stack:
    """Stack to keep nodes in order."""

    def __init__(self):
        self.root = None

    def is_empty(self) -> bool:
        """Check whether the stack is empty or not."""
        return True if self.root is None else False

    def push(self, node_id: int):
        """Push a node into the stack."""
        if isinstance(node_id, int):
            node = Node(node_id)
            if self.root is None:
                self.root = node
            else:
                node.next = self.root
                self.root = node
        else:
            print("Node id must be integer!")

    def pop(self):
        """Pop a node from the stack."""
        if not self.is_empty():
            temp = self.root
            self.root = temp.next
            return temp.data
        return -1

    def peek(self):
        """Peek a node from the stack."""
        if not self.is_empty():
            return self.root.data
        return -1

    def size(self):
        """Size of the stack."""
        stack_size = 0
        current = self.root
        while current:
            stack_size += 1
            current = current.next
        return stack_size

    def display(self):
        """Display all nodes in the stack."""
        current = self.root
        while current:
            print(f"Node {current}")
            current = current.next
        print("************************************")


def print_selection():
    """Selection list."""
    print("************************************")
    print(
        "1-Push a node into the stack.\n"
        "2-Pop a from the stack.\n"
        "3-Peek a node from in the stack.\n"
        "4-Is Empty.\n"
        "5-Show the size of the stack\n"
        "6-Display all the nodes of the stack.\n"
        "7-Exit.\n"
    )
    print("************************************")


def main():
    """Main program for stack operations."""
    stack_list = Stack()
    while True:
        try:
            print_selection()
            selection = input("Enter your selection:")

            if selection == "1":
                node_id = int(input("Enter node id:"))
                stack_list.push(node_id)
            elif selection == "2":
                if stack_list.is_empty():
                    print("There is no node to pop in the stack!")
                else:
                    print(f"The node {stack_list.pop()} is popped.")
            elif selection == "3":
                if stack_list.is_empty():
                    print("There is no node to peek in the stack!")
                else:
                    print(f"The node {stack_list.peek()} is peeked.")
            elif selection == "4":
                print("The pop ")
                print(stack_list.is_empty())
            elif selection == "5":
                print(f"The size of the stack is {stack_list.size()}")
            elif selection == "6":
                stack_list.display()
            elif selection == "7":
                break
            else:
                print("The selection is invalid!")
        except ValueError:
            print("You must enter integer value for node id!")


if __name__ == "__main__":
    main()
