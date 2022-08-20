# how to find the sum of digits of a positive integer number using recursion


x = 534709143453434545


def sum_of_digits(num):
    if num == 0:
        return num
    else:
        return int(sum_of_digits(num / 10)) + (num % 10)


print(f"Sum of the numbers is {sum_of_digits(x)}")
