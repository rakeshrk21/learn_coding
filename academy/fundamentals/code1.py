from enum import unique


def tester(*args, **kwargs):
    sum = 0
    for num in args:
        sum += num
    print("sum", sum)
    for key, value in kwargs.items():
        print(key, value)


def prints(nums):
    for num in nums:
        print(num)

def two_sum(nums, target):
    charMap = dict()

    for index, num in enumerate(nums):
        complement = target - num
        if complement in charMap:
            return (complement, num)
        else:
            charMap[num] = index

    return (-1, -1)

def print_repeated(s):
    charMap = dict()
    if len(s) <=1:
        return -1

    for i in range(len(s)):
        c = s[i]
        if c in charMap:
            return charMap[c][1]
        else:
            charMap[c] = (i, c)

    return -1

def min_max_unsorted(nums):

    if len(nums) <1:
        return
    elif len(nums) ==1:
        return (nums[0], nums[0])

    min = max = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > max:
            max = nums[i]
        elif nums[i] < min:
            min = nums[i]

    return (min, max)

def find_duplicates(nums):
    seen = set()
    unique= set()

    for num in nums:
        if num not in unique:
            unique.add(num)
        else:
            seen.add(num)

    return seen

def reverse_string(str):
    li = list(str)
    for i in range(len(str)//2):
        li[i], li[-1-i] = li[-1-i], li[i]
    return ''.join(li)

add = lambda *args: sum(args)
lambda **kwargs: print(f"{key}")



if __name__ == "__main__":
    tester(1, 3, 9, name="rakesh", age="47")
    nums = [i*2 for i in range(1,10) ]
    print(nums)
    prints(nums)
    items = ['apple', 'banana', 'cherry']
    for k, v in enumerate(items):
        print(k, v)

    nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    print(two_sum(nums1, 30))
    print(print_repeated("rakesaehh"))
    print(min_max_unsorted([2, 43, 16, 18, -10, 1, 14, 5, 18]))
    print(min_max_unsorted([1]))
    print(find_duplicates([2, 43, 16, 18, -10, -10, 14, 5, 5, 18]))
    print(reverse_string("rakesh"))
    nums1.append(59)
    nums1.insert(3, 66)
    print(nums1.pop())
    print(nums1)
    print(nums1.append(59))
    print(nums1.reverse())
    print(nums1.remove(14))
    print(nums1)
    m = [i*1 for i in range(-1,101)]
    print(m)
    print(add(5, 7, 9))

