class Jar:
    def __init__(self, capacity=12, size=0):
        if capacity <= 0:
            raise ValueError
        self.capacity = capacity
        self.size = size

    def __str__(self):
        amount = '🍪' * self.size
        return f'{amount}'

    def deposit(self, n):
        if (n  + self.size) > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
