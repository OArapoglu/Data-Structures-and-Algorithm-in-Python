"""
QUEUE OPERATIONS
    Create a node from Node including data and next properties.
    EnQueue a node into queue.
    DeQueue a node from the queue.
    IsEmpty the queue.
    IsFull the queue.
    Front node of the queue.
    Rear node of the queue.
    Print all nodes in the queue.
"""


class Node:
    """A data structure to keep a data and next pointer."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Queue:
    """Queue to keep nodes in order."""
    def __init__(self, capacity: int):
        self.front = self.rear = None
        self.capacity = capacity

    def enqueue(self, node_id: int):
        """Add a node to the queue."""
        if isinstance(node_id, int):
            node = Node(node_id)
            if not self.is_full():
                if self.rear is None:
                    self.front = self.rear = node
                else:
                    self.rear.next = node
                    self.rear = node
            else:
                print("The capacity is full!")
        else:
            print("Node id must be integer!")

    def dequeue(self):
        """Remove a node to the queue."""
        if self.front:
            self.front = self.front.next
            if self.front is None:
                self.rear = None
        else:
            print("There is no node!")

    def size(self):
        """Size of the queue."""
        queue_size = 0
        current = self.front
        while current:
            queue_size += 1
            current = current.next
        return queue_size

    def is_empty(self) -> bool:
        """Check whether the queue is empty or not."""
        return True if self.front is None else False

    def is_full(self) -> bool:
        """Check whether the queue is empty or not."""
        return True if self.capacity == self.size() else False

    def front_node(self) -> int:
        """Check whether the queue is empty or not."""
        return self.front.data

    def rear_node(self) -> int:
        """Check whether the queue is empty or not."""
        return self.rear.data

    def display(self):
        """Print current nodes in the linked list."""
        current = self.front
        while current is not None:
            print(f"Node {current}")
            current = current.next
        print("************************************")


def print_selection():
    """Selection list."""
    print("************************************")
    print(
        "1-Enqueue a node.\n"
        "2-Dequeue a node.\n"
        "3-IsEmpty the queue.\n"
        "4-IsFull the queue.\n"
        "5-Front node.\n"
        "6-Rear node.\n"
        "7-Size of the queue.\n"
        "8-Display all nodes of your linked list.\n"
        "9-Exit.\n"
    )
    print("************************************")


def main():
    """Main program for queue operations."""
    CAPACITY = 5
    queue = Queue(CAPACITY)
    while True:
        try:
            print_selection()
            selection = input("Enter your selection:")
            if selection == "1":
                node_id = int(input("Enter node id:"))
                queue.enqueue(node_id)
            elif selection == "2":
                queue.dequeue()
            elif selection == "3":
                print(queue.is_empty())
            elif selection == "4":
                print(queue.is_full())
            elif selection == "5":
                print(queue.front_node())
            elif selection == "6":
                print(queue.rear_node())
            elif selection == "7":
                print(f"The size of the queue is {queue.size()}")
            elif selection == "8":
                queue.display()
            elif selection == "6":
                break
            else:
                print("The selection is invalid!")
        except ValueError:
            print("You must enter integer value for node id!")


if __name__ == "__main__":
    main()
