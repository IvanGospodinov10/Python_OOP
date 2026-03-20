class vowels:
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

    def __init__(self, text):
        self.text = text
        self.counter = -1
        # --- without recursion ---
        # self.vowels = [el for el in self.text if el.lower() in self.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1

        if self.counter >= len(self.text):
            raise StopIteration

        if self.text[self.counter].lower() in self.VOWELS:
            return self.text[self.counter]
        else:
            return  self.__next__()

    # --- without recursion ---

    # def __next__(self):
    #     self.counter += 1
    #     if self.counter >= len(self.VOWELS):
    #         raise StopIteration
    #     else:
    #         return self.vowels[self.counter]




my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
