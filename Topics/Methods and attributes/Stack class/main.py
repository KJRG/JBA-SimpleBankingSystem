class Stack():

    def __init__(self):
        self._list = list()

    def push(self, el):
        self._list.append(el)

    def pop(self):
        return self._list.pop(-1)

    def peek(self):
        return self._list[-1]

    def is_empty(self):
        return not bool(self._list)
