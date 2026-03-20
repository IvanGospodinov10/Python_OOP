class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.counter = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.counter -= 1
        if self.counter >= 0:
            return self.iterable[self.counter]
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
