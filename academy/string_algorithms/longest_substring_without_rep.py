from turtledemo.sorting_animate import start_isort


def longest_substring_without_repeated_characters(str):

    start = end = start_index = max_length = 0
    sett = set()

    while end < len(str):

        c = str[end]
        if c not in sett:
            sett.add(c)
            end += 1

            # update the maxlength
            if end - start > max_length:
                max_length = end - start
                start_index = start

        else:
            sett.remove(str[start])
            start += 1

    return str[start_index:start_index+max_length]

if __name__ == "__main__":
    print(longest_substring_without_repeated_characters("pwwkew"))
