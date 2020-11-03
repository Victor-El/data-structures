from types import TracebackType
from typing import Optional


class ListNode:

    def __init__(self, value):
        self.__value = value
        self.__next = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node

    def __repr__(self):
        return f"[ val: {self.__value}, next: {self.__next} ]"


# Custom exception class for LinkedList
class IndexOutOfBoundException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def with_traceback(self, tb: Optional[TracebackType]) -> BaseException:
        return super().with_traceback(tb)


class LinkedList:

    def __init__(self):
        self.__head: ListNode = None
        self.__count: int = 0

    @property
    def count(self):
        return self.__count

    def add(self, val) -> None:

        if self.__head is None:
            self.__head = ListNode(val)
            self.__count += 1
        else:
            current = self.__head
            while current.next:
                current = current.next

            current.next = ListNode(val)
            self.__count += 1

    def remove(self, index: int) -> None:
        if index > self.__count - 1:
            raise IndexOutOfBoundException(f"index {index} bigger than list of length {self.count}")

        elif index == 0:
            self.__head = self.__head.next
            self.__count -= 1

        else:
            current = self.__head
            for i in range(self.__count):
                if i == index - 1:
                    current.next = current.next.next
                    self.__count -= 1
                    break
                current = current.next

    def get(self, index: int) -> object:

        if self.__head is None:
            raise IndexOutOfBoundException("List is empty")

        if index > self.__count - 1:
            raise IndexOutOfBoundException(f"index {index} bigger than list of length {self.count}")
        elif index == 0:
            return self.__head.value
        else:
            current = self.__head.next
            counter = 1
            if counter == index:
                return current.value
            while current:
                current = current.next
                counter += 1
                if counter == index:
                    return current.value

    def insert_at(self, obj: object, index: int) -> None:
        if index > self.__count - 1:
            raise IndexOutOfBoundException("Index larger than array size")

        elif index == 0:
            current_head = self.__head
            new_node = ListNode(obj)
            new_node.next = current_head
            self.__head = new_node
            self.__count += 1

        else:
            new_node = ListNode(obj)
            counter = 0
            current = self.__head

            while current:
                if counter == index - 1:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
                counter += 1
            self.__count += 1

    def add_first(self, val: object) -> None:
        current_head = self.__head
        self.__head = ListNode(val)
        self.__head.next = current_head
        self.__count += 1

    def add_last(self, val: object) -> None:
        if self.__head is None:
            self.__head = ListNode(val)
            return
        current = self.__head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.__count += 1

    def remove_first(self) -> None:
        current_head = self.__head
        self.__head = current_head.next
        self.__count -= 1
        del current_head

    def remove_last(self) -> None:
        self.remove(self.__count - 1)

    def clear(self) -> None:
        self.__head = None
        self.__count = 0

    def get_first(self) -> object:
        if self.__count == 0:
            return None
        return self.__head.value

    def get_last(self) -> object:
        if self.__count == 0:
            return None
        current = self.__head
        while current.next:
            current = current.next
        return current.value

    def search(self, obj: object) -> int:
        if self.__head is None:
            return -1

        elif self.__head.next is None:
            if self.__head.value == obj:
                return 0

        else:
            current = self.__head
            index = 0
            while current:
                if current.value == obj:
                    return index
                current = current.next
                index += 1

            return -1

    def sort(self) -> None:
        if self.__head is None or self.__head.next is None:
            return
        new_linked_list = None
        first_node = None
        compare_node = self.__head
        smallest = self.__head.value
        previous = None
        smallest_node_parent = None

        while compare_node:
            current = compare_node
            while current:
                if current.value < smallest:
                    smallest = current.value
                    smallest_node_parent = previous
                previous = current
                current = current.next

            compare_node = compare_node.next

            if new_linked_list is None:
                first_node = ListNode(smallest)
                new_linked_list = first_node
                smallest_node_parent.next = smallest_node_parent.next.next
                smallest = compare_node.value
            else:
                new_linked_list.next = ListNode(smallest)
                new_linked_list = new_linked_list.next
                if smallest_node_parent.next.next:
                    smallest_node_parent.next = smallest_node_parent.next.next
                    smallest = compare_node.value

        self.__head = first_node

    def reverse(self) -> None:

        if self.__head is None or self.__head.next is None:
            return

        last_node = None
        previous_node = None
        head = self.__head
        first_node = None

        while True:
            while head.next.next:
                head = head.next
            previous_node = head
            last_node = previous_node.next
            if first_node is None:
                first_node = last_node
            last_node.next = previous_node
            previous_node.next = None
            head = self.__head
            if self.__head.next is None:
                last_node.next = self.__head
                self.__head = first_node
                break

    def __repr__(self):
        return f"{self.__head}"


if __name__ == "__main__":
    li: LinkedList = LinkedList()
    for i in range(300):
        li.add(i)
    print(li.get(0))
    print("LinkedList is {size} items long".format(size=li.count))
    li = "End"
    print(li)

