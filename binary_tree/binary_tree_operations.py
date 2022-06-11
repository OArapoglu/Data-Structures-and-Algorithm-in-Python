"""
BINARY TREE
Each node has at most two children.
The value of left node is lower than the parent node whereas the value of right node is greater than the parent node.
Insert a node into binary binary_tree.
Preorder Traverse
Inorder Traverse
PostOrder Traverse
"""


class Node:
    """A data structure to keep a data and next pointer."""

    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    """Create and traverse a binary tree."""

    def __init__(self):
        self.root = None

    def insert(self, node_id: int, current: Node = None):
        """Insert a node into the binary tree."""
        if isinstance(node_id, int):
            node = Node(node_id)
            if self.root is None:
                self.root = node
            else:
                if current is None:
                    current = self.root
                if node.data < current.data:
                    if current.left is None:
                        current.left = node
                    else:
                        self.insert(node_id, current.left)
                elif node.data > current.data:
                    if current.right is None:
                        current.right = node
                    else:
                        self.insert(node_id, current.right)
        else:
            print("Node id must be integer!")

    def preorder_traverse(self, current: Node = None):
        """Visit the nodes with preorder in the binary tree."""
        if current is None:
            current = self.root
        print(current.data)
        if current.left:
            self.preorder_traverse(current.left)
        if current.right:
            self.preorder_traverse(current.right)

    def inorder_traverse(self, current: Node = None):
        """Visit the nodes with inorder in the binary tree."""
        if current is None:
            current = self.root
        if current.left:
            self.inorder_traverse(current.left)
        print(current.data)
        if current.right:
            self.inorder_traverse(current.right)

    def postorder_traverse(self, current: Node = None):
        """Visit the nodes with postorder in the binary tree."""
        if current is None:
            current = self.root
        if current.left:
            self.postorder_traverse(current.left)
        if current.right:
            self.postorder_traverse(current.right)
        print(current.data)


def print_selection():
    """Selection list."""
    print("************************************")
    print(
        "1-Insert a node into the binary binary_tree.\n"
        "2-Preorder Traverse.\n"
        "3-Inorder Traverse.\n"
        "4-Postorder Traverse.\n"
        "5-Exit.\n"
    )
    print("************************************")


def main():
    """Main program for binary_tree operations."""
    binary_tree = BinaryTree()
    while True:
        try:
            print_selection()
            selection = input("Enter your selection:")
            if selection == "1":
                node_id = int(input("Enter node id:"))
                binary_tree.insert(node_id)
            elif selection == "2":
                binary_tree.preorder_traverse()
            elif selection == "3":
                binary_tree.inorder_traverse()
            elif selection == "4":
                binary_tree.postorder_traverse()
            elif selection == "5":
                break
            else:
                print("The selection is invalid!")
        except ValueError:
            print("You must enter integer value for node id!")


if __name__ == "__main__":
    main()






