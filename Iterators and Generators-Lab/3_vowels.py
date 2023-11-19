class vowels:
    def __init__(self, string):
        self.string = string
        vowels_ = ["a", "e", "i", "u", "y", "o"]
        self.vowels_list = [v for v in self.string if v.lower() in vowels_]
        self.current_index = 0
        self.end_index = len(self.vowels_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.end_index:
            raise StopIteration()
        index = self.current_index
        self.current_index += 1
        return self.vowels_list[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

