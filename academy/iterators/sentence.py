class Sentence:

    def __init__(self, sentence):
        self.words = sentence.split()
        self.index = 0

    def __iter__(self):
        return self

    # for make a class iterable we need a __next__
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        current = self.index
        self.index += 1
        return self.words[current]


def sentence(sentence):
    for w in sentence.split():
        yield w


my_sentence = Sentence("This is a test")
for word in my_sentence:
    print(word)

g = sentence("This is a test")
for item in g:
    print(item)

# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))

