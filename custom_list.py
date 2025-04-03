class CustomList:
    def __init__(self):
        self._data = []
    
    def length(self) -> int:
        return len(self._data)
    
    def append(self, element: str) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")
        self._data.append(element)
    
    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self.length():
            raise IndexError("Index out of bounds")
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")
        self._data.insert(index, element)
    
    def delete(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise IndexError("Index out of bounds")
        return self._data.pop(index)
    
    def deleteAll(self, element: str) -> None:
        self._data = [e for e in self._data if e != element]
    
    def get(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise IndexError("Index out of bounds")
        return self._data[index]
    
    def clone(self) -> 'CustomList':
        new_list = CustomList()
        new_list._data = self._data.copy()
        return new_list
    
    def reverse(self) -> None:
        self._data.reverse()
    
    def findFirst(self, element: str) -> int:
        try:
            return self._data.index(element)
        except ValueError:
            return -1
    
    def findLast(self, element: str) -> int:
        for i in reversed(range(self.length())):
            if self._data[i] == element:
                return i
        return -1
    
    def clear(self) -> None:
        self._data = []
    
    def extend(self, elements: 'CustomList') -> None:
        self._data.extend(elements._data)
