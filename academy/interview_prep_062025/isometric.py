# check for isometric strings egg --- add are isometric
# forward mapping and reverse mapping should be unique i.e.  e <-> a, g <-> d and i.e a <-> e, d <-> g.
# if this rules breaks then the strings are not isometric

# conditions the strings should meet
# if length of the strings are unequal then not isometric
# each char in string#1 should uniquely match with each character in string#2
# each char in string#2 should uniquely match with each character in string#1

def is_isometric(s1, s2):
    forward = dict()
    reverse = dict()

    # if length of the strings are unequal then not isometric
    if len(s1) != len(s2):
        return False

    # iterate the strings
        # append each char from string1 as key and each char to string2 as value on dict1
           # if the key exists and the value does not match to the key of string2, return False
           # if the key exists and the value matches, just skip and continue (nothing to be done)
           # if the key does not exist then just append the key, value pair to the dict1
        # append each char from string2 as key and each char to string1 as value on dict2

    for c1, c2 in zip(s1, s2):

        if c1 in forward:
            if c2 != forward[c1]:
                return False
        else:
            forward[c1] = c2

        # is better than if c1 in forward.keys() You don't need .keys() when checking key existence:
        if c2 in reverse.keys():
            if c1 != reverse[c2]:
                return False
        else:
            reverse[c2] = c1

    return True


if __name__ == "__main__":
    print(is_isometric('egg', 'add')) # True
    print(is_isometric('paper', 'title'))  # True
    print(is_isometric('foo', 'bar'))  # False
    print(is_isometric('ab', 'aa'))  # False
    print(is_isometric('address', 'nniilok'))  # False
    print(is_isometric("ab", "cc") ) # False (a and b both map to c)