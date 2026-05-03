from itertools import compress
from re import split
from typing import List
from unicodedata import digit


class StringProblems:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = k = 0
        s = ""

        while i < len(word1) and k < len(word2):
            s = s + word1[i] + word2[k]
            i += 1
            k += 1

        while i < len(word1):
            s = s + word1[i]
            i += 1

        while k < len(word2):
            s = s + word2[k]
            k += 1

        return s

    def compress1(self, chars: List[str]) -> tuple:
        l = list()
        map = dict()
        for i in range(len(chars)):
            c = chars[i]
            if c in map:
                map[c] = map.get(c) + 1
            else:
                map[c] = 1

        chars.clear()

        for k, v in map.items():
            if v == 1:
                chars.append(k)
            else:
                chars.append(k)
                if v > 9:
                    li = [digit for digit in str(v)]
                    for i in li:
                        chars.append(i)
                else:
                    chars.append(v)



        return (len(chars), chars)

    def compress(self, chars: List[str]) -> tuple:

        left = right = 0

        while right < len(chars):

            c = chars[right] # read the first character
            count = 0 # set count to 0

            while right < len(chars) and chars[right] == c:
                right += 1 # keep moving the right pointer to find the last repeated character
                count += 1 # increment count

            chars[left] = c  # store the character at left
            left += 1 # skip the first character

            if count > 1:
                for digit in str(count):
                    chars[left] = digit
                    left += 1

        # Remove extra characters beyond the new compressed length
        while len(chars) > left:
            chars.pop()

        return (len(chars), chars)

    def reverseVowels(self, s: str) -> str:
        a = list(s)
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        left = 0
        right = len(a)-1
        while left < right:
            if a[left] not in vowels:
                left += 1
            if a[right] not in vowels:
                right -= 1
            if a[left] in vowels and a[right] in vowels:
                temp = a[right]
                a[right] = a[left]
                a[left] = temp
                left += 1
                right -= 1

        return ''.join(a)

    def reverseWords(self, s: str) -> str:
        a = s.split(' ')
        a = [x for x in a if x.strip()]
        left = 0
        right = len(a)-1
        while left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1

        return ' '.join(a)

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n > 0 and len(flowerbed) == 1 and flowerbed[0] == 0:
            n = n-1
            return n == 0

        left = 0
        right = 1
        end = len(flowerbed) - 1


        while n > 0 and right <= end:

            if left == 0 and flowerbed[left] == 0 and flowerbed[right] == 0:
                flowerbed[left] = 1
                n = n - 1

            elif flowerbed[left] == 0 and flowerbed[left-1] == 0 and flowerbed[right] == 0:
                flowerbed[left] = 1
                n = n - 1

            elif right == end and flowerbed[left] == 0 and flowerbed[right] == 0:
                flowerbed[right] = 1
                n = n - 1

            right = right + 1
            left = left + 1


        print(flowerbed)
        print(n)
        return n == 0


if __name__ == "__main__":
    sp = StringProblems()
    # print(sp.mergeAlternately("abcd", "pq"))
    # print(sp.compress(["a", "a", "b", "b", "c", "c", "c"]))
    # print(sp.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
    # print(sp.reverseVowels("IceCreAm"))
    # print(sp.reverseWords("  hello   world  "))

    print(sp.canPlaceFlowers([1,0,0,0,1], 1))
    print(sp.canPlaceFlowers([0,0,1,0,1], 1))
    print(sp.canPlaceFlowers([1,0,1,0,0], 1))

