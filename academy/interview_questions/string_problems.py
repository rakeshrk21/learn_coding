def reverseStr(str):
    reverse = ''
    for i in range(len(str)-1, -1, -1):
        reverse += str[i]
    print(reverse)

def test_for_loop():
    for i in range(5, 0, -1):
        print(f'Before manual change: {i}')
        i = i + 1
        print(f'After manual change: {i}')

def string_is_palindrome(str):
    i = 0
    j = len(str)-1

    while i<j:
        if str[i] != str[j]:
            return False
        else:
            return True
        
def two_sum(li, total):
    seen = {}
    for i in range(len(li)):
        compliment = total - li[i]
        if compliment in seen:
            return (li[i], compliment)
        else:
            seen[li[i]] = i 
    return (-1, -1)

def find_repeated_characters(str):
    repeated = {}
    for i in range(len(str)):
        if str[i] in repeated:
            repeated[str[i]] = repeated[str[i]] +1
        else:
            repeated[str[i]] = 1
    
    for key, value in repeated.items():
        if value >1:
            print(key)
  
if __name__ == '__main__':
    reverseStr('rakesh')
    test_for_loop()
    print(string_is_palindrome('racecar'))
    print(two_sum([2, 7, 11, 15, 21, 3, 9], 10))
    print(find_repeated_characters("abcdeeda"))