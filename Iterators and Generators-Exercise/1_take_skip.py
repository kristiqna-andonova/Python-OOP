class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.count:
            raise StopIteration()
        else:
            current = self.index * self.step
            self.index += 1
            return current


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

