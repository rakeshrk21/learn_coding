# binary search is search an element in a sorted array. It uses divide and conquer principle


def binary_search(arr, low, high, num):

    if low <= high:

        m = (low + high) // 2

        if arr[m] == num:
            return m

        elif arr[m] > num:
            return binary_search(arr, low, m-1, num)

        else:
            return binary_search(arr, m+1, high, num)

    else:
        # Element is not present in the array
        return -1


if __name__ == "__main__":
    a = [2, 7, 12, 25, 66, 102, 432, 542, 667, 789, 972, 999, 1032, 1789, 1924]
    print(binary_search(a, 0, len(a)-1, 542))

