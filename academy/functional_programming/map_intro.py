import timeit

text = "what is the responsibility of the QA person?"


def comp_caps():
    return [c.upper() for c in text]


# use map to print capital characters
def map_caps():
    return list(map(str.upper, text))


def comp_words():
    return [word.upper() for word in text.split(' ')]


# use map to print capital word
def map_words():
    return list(map(str.upper, text.split()))


if __name__ == '__main__':
    print(map_words())
    print(comp_words())
    print(map_caps())
    print(comp_caps())
    print(timeit.timeit(map_words, number=100000))
    print(timeit.timeit(comp_words, number=100000))
