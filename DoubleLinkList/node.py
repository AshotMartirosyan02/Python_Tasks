class Node:
    def __init__(self, data: int) -> None:
        self._data: int = data
        self._next = None
        self._prev = None

    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, value: int) -> None:
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value) -> None:
        self._next = value

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, value) -> None:
        self._prev = value
