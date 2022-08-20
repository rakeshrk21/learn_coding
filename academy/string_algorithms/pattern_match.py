def match_pattern(text, pattern):
    l = len(text)
    p = len(pattern)
    if p > l:
        return "pattern not found!"
    else:
        for i in range(l-1):
            if i + p <= l and text[i:i+p] == pattern:
                return f'pattern found at index {i}'
        return "pattern not found!"


if __name__ == "__main__":
    print(match_pattern("golddigger", "gold"))
    print(match_pattern("arkinojk", "jk"))
    print(match_pattern("repirotary", "tary"))
    print(match_pattern("repirotary", "iro"))
    print(match_pattern("repirotary", "irok"))