class Stack:
    def __init__(self, items=None, limit=100):
        # avoid mutable default
        if items is None:
            self.items = []
        else:
            self.items = list(items)   # make a copy
        self.limit = limit

    def isEmpty(self):
        """Return True if the stack is empty"""
        return len(self.items) == 0

    def push(self, item):
        """Push an item to the stack if not full"""
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        """Remove and return the top item; return None if empty"""
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it"""
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        """Return the number of elements in the stack"""
        return len(self.items)

    def full(self):
        """Return True if stack is full"""
        return len(self.items) >= self.limit

    def search(self, target):
        """
        Return distance from top to target if found, else -1.
        Top element = distance 0.
        """
        try:
            index_from_bottom = self.items.index(target)
            return (len(self.items) - 1) - index_from_bottom
        except ValueError:
            return -1