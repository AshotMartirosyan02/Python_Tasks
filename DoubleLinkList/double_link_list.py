from node import Node


class DoubleLinkList:
    def __init__(self) -> None:
        self._head = None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node) -> None:
        self._head = node


    def is_empty(self) -> bool:
        return self.head == None

    def append(self, data: int) -> None:
        new = Node(data)
        if self.head is None:
            self.head = new
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new
        new.prev = current

    def prepend(self, data: int) -> None:
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def insert_before(self, target_data: int, data: int) -> None:
        if self.head is None:
            print("List empty")
            return
        current = self.head
        while current.data != target_data and current is not None:
            current = current.next
        if current is None:
            print("chka listi mej")
            return

        new = Node(data)
        new.prev = current.prev
        new.next = current
        if current.prev is not None:
            current.prev.next = new
        else:
            self.head = new

        current.prev = new

    def insert_after(self, target_data: int, data: int) -> None:
        if self.head is None:
            print("List empty")
            return
        current = self.head
        while current.data != target_data and current is not None:
            current = current.next

        if current is None:
            print("chka listi mej")
            return

        new = Node(data)
        new.next = current.next
        new.prev = current

        if current.next is not None:
            current.next.prev = new

        current.next = new

    def delete(self, data: int) -> str:
        if self.head is None:
            return "There is no data to delete in empty list"

        current = self.head

        while current is not None:
            if current.data == data:
                if current.next is not None:
                    current.next.prev = current.prev
                if current.prev is not None:
                    current.prev.next = current.next
                if current == self.head:
                    self.head = current.next
                current.data = None
                current.prev = None
                current.next = None
                return f"{data} deleted in this list"
            current = current.next
        return  "Data not found in this list"

    def display(self) -> None:
        if self.head is None:
            print("List empty")
            return

        current = self.head
        while current:
            print(current.data, end=", ")
            current = current.next
