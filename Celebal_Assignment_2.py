class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        if not self.head:
            print("The list is empty.")
            return

        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise ValueError("Index must be a positive integer.")

        if n == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            print(f"Deleted node at position 1 with value {deleted_data}")
            return

        current = self.head
        count = 1
        while current and count < n - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            raise IndexError(f"Index {n} is out of range.")

        deleted_data = current.next.data
        current.next = current.next.next
        print(f"Deleted node at position {n} with value {deleted_data}")

ll = LinkedList()

ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)
print("Initial list:")
ll.print_list()

ll.delete_nth_node(3)
print("List after deleting 3rd node:")
ll.print_list()

try:
    ll.delete_nth_node(10)
except Exception as e:
    print("Exception:", e)

empty_list = LinkedList()
try:
    empty_list.delete_nth_node(1)
except Exception as e:
    print("Exception:", e)
