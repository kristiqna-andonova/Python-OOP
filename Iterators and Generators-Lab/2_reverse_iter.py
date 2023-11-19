class reverse_iter:
    def __init__(self, collection):
        self.collection = collection
        self.start = len(self.collection) - 1
        self.end = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            raise StopIteration()
        current = self.start
        self.start -= 1
        return self.collection[current]
