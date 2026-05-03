    # write a program to find all pairs of integers whose sum is equal to a given number e.g 9 -> [6,3)


def bf_solution_sum_of_pairs_equals_target(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    return pairs


def solution_sum_of_pairs_equals_target(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    return pairs


# find missing number in a integer array of 1 to 100
def find_missing_number_in_integer_array(nums):
    missing_numbers = []

    for i in range(1, 101):
        found = False
        for num in nums:
            print(num)
            if i == num:
                found = True
                break
        if not found:
            found = False
            missing_numbers.append(i)
    return missing_numbers


# find the maximum product of two integers in an array where all elements are positive
def bf_find_pair_which_has_the_greatest_product(nums):
    target = 0
    pair = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            temp = nums[i] * nums[j]
            if temp > target:
                target = temp
                pair = [nums[i], nums[j]]
    return target, pair


# how to test


# implement an algo to determine if all items of the list are unique
def bf_check_if_list_is_unique(nums):
    repeated_items = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                repeated_items.append(nums[i])
    return (len(repeated_items), repeated_items)


# find max and 2nd max numbers from an array.
def find_max_and_second_max(nums):
    max1 = 0
    max2 = 0
    for i in range(len(nums)):
        if nums[i] > max1:
            max1 = nums[i]
        elif nums[i] > max2:
            max2 = nums[i]

    return (max1, max2)


# Convert "23" into its binary Equivalent
def convert_number_into_binary(num):
    binary = []
    q = num
    r = None
    while q != 0:
        r = q % 2
        q = int(q / 2)
        binary.insert(0, r)
    print(binary)
    return binary


def convert_binary_to_decimal(nums):
    decimal = 0
    j = 0

    for i in range(len(nums) - 1, -1, -1):
        decimal = decimal + (2 ** j * nums[i])
        j = j + 1
    return decimal


# find if two strings are permutations of each other
def check_if_two_strings_are_permutations_of_each_other(str1, str2):
    if (len(str1) != len(str2)):
        return False
    for i in range(len(str1)):
        found = False
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                found = True
                break
        if not found:
            return False
    return True


# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator. return the quotient

def divide_two_integers(divident, divisor):
    count = 0
    while (divident >= divisor):
        rem = divident - divisor
        count += 1
        divident = rem
    return count


# how do you find out if a number is prime?
def is_number_prime_numbers(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


# Palindrome of a String with special chars and alphanumeric - Ignore special Chars and find palindrome or not.
def is_the_string_palindrome(str1, str2):
    return False


# Isometric strings e.g. ACAB == XCXY
def is_isometric(a, b):
    # if the length is not equal return false
    if len(a) != len(b):
        return False

    # define a dictionary. char's in a are the key while chars in b are values
    d = dict()

    for i in range(len(b)):
        if b[i] in d.values():  # if the char in string b exists in the dict
            for k, v in d.items():
                if b[i] == v and k == a[i]:  # check matching k,v pair was found in the dictionary
                    break
        elif b[i] not in d.values() and a[i] not in d.keys():
            d[a[i]] = b[i]  # insert the key,value pair in the dict but if the key was used, key error, so return false
            continue  # continues the for loop
        else:
            return False
    return True
    #
    # # Min max of array
    # # User function Template for python3
    #
    # def get_min_max(self, arr):
    #     if len(arr) == 1:
    #         min = arr[0]
    #         max = arr[0]
    #         return min, max
    #     if arr[0] < arr[1]:
    #         min = arr[0]
    #         max = arr[1]
    #     else:
    #         min = arr[1]
    #         max = arr[0]
    #     for i in range(2, len(arr)):
    #         if arr[i] < min:
    #             min = arr[i]
    #         if arr[i] > max:
    #             max = arr[i]
    #
    #     return min, max



if __name__ == '__main__':
    # nums = [2, 4, 1, 6, 5, 10, -1, -2, -5, 3, 9, 0]
    # print(bf_solution_sum_of_pairs_equals_target(nums, 15))
    #
    # li = [1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 135, 16, 27, 58, 19, 21]
    # print(bf_find_pair_which_has_the_greatest_product(li))
    #
    # check_uniqueness = [1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21, 35]
    # print(bf_check_if_list_is_unique(check_uniqueness))

    my_list = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
               30, 31,
               32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59,
               60,
               61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87,
               88, 89,
               90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    # print(find_missing_number_in_integer_array(my_list))
    #
    # print(find_max_and_second_max([77,62, 403, 99, -25, 0, 735]))
    #
    # print(convert_number_into_binary(23))
    #
    # print(convert_binary_to_decimal([1,0,1,1,1]))
    #
    # print(check_if_two_strings_are_permutations_of_each_other("apple", "papel"))

    # print(divide_two_integers(10,3))
    # print(divide_two_integers(25,5))
    # print(divide_two_integers(7,-3))
    #

    # print(is_number_prime_numbers(3))
    # st1 = "TEx1t"
    # print(st1.lower())
    # print(st1.upper())
    # print(st1.isalpha())
    # print(st1.isalnum())

    # print(is_isometric("ACAB", "XCXY")) # test pass
    # print(is_isometric("ACAB", "XCRY")) # test fail
    # print(is_isometric("paper", "title")) # test pass
    # print(is_isometric("foo", "app")) # test pass
    print(is_isometric("ab", "aa"))  # test fail (needs fix)
