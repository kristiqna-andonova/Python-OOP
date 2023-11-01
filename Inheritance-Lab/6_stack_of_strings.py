class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)
        else:
            raise ValueError

    def pop(self):
        element = self.data.pop()
        return element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        else:
            return True

    def __str__(self):
        reverse = reversed(self.data)
        return f"[{', '.join(reverse)}]"


