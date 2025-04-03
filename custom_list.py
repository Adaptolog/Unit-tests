class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CustomList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def length(self) -> int:
        return self._length

    def append(self, element: str) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")
        
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self._length:
            raise IndexError("Index out of bounds")
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")
        
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        elif index == self._length:
            self.append(element)
            return
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
        
        self._length += 1

    def delete(self, index: int) -> str:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            data = current.data
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            else:
                self.tail = current.prev
        
        self._length -= 1
        return data

    def deleteAll(self, element: str) -> None:
        current = self.head
        while current:
            if current.data == element:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self._length -= 1
            current = current.next

    def get(self, index: int) -> str:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def clone(self) -> 'CustomList':
        new_list = CustomList()
        current = self.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list

    def reverse(self) -> None:
        current = self.head
        while current:
            next_node = current.next
            current.next, current.prev = current.prev, current.next
            current = next_node
        self.head, self.tail = self.tail, self.head

    def findFirst(self, element: str) -> int:
        index = 0
        current = self.head
        while current:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1

    def findLast(self, element: str) -> int:
        index = self._length - 1
        current = self.tail
        while current:
            if current.data == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self) -> None:
        self.head = self.tail = None
        self._length = 0

    def extend(self, elements: 'CustomList') -> None:
        clone = elements.clone()
        if self.head is None:
            self.head = clone.head
            self.tail = clone.tail
        else:
            self.tail.next = clone.head
            if clone.head:
                clone.head.prev = self.tail
                self.tail = clone.tail
        self._length += clone._length
