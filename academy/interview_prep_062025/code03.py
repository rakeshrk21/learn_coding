def isPalindrome(str):
    lower_string = str.lower()
    count = len(lower_string)
    for i in range(len(lower_string)):
        print(i)
        print(lower_string[i])
        print(lower_string[count-i-1])
        if lower_string[i] != lower_string[count-i-1]:
            return False
    return True


def is_isometric(str1, str2):

    if len(str1) != len(str2):
        return False

    mapping = {}
    used = []

    for c1, c2 in zip(str1, str2):
        # check c1 is in the map and the value is c2
        if c1 in mapping:
            if mapping[c1] != c2:
                return False

        elif c2 in used:
            return False

        else:
            mapping[c1] = c2
            used.append(c2)

    return True


if __name__ == '__main__':
    # print(isPalindrome('malayalam'))
    print(is_isometric('egg', 'dkk'))  # True
    print(is_isometric('foo', 'bar'))  # False
    print(is_isometric('paper', 'title'))  # True
    print(is_isometric('address', 'nniilok'))  # False
    print(is_isometric("ab", "cc") ) # False (a and b both map to c)