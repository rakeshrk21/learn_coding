import math

def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    print(l)


def selection_sort(l):
    for i in range(len(l)-1):
        min_index = i
        for j in range(i+1, len(l)-1):
            if l[j] < l[min_index]:
                l[min_index], l[j] = l[j], l[min_index]
    print(l)


def insertion_sort(l):
    for i in range(len(l)-1):
        while i > 0:
            if l[i] < l[i-1]:
                l[i], l[i-1] = l[i-1], l[i]
            i -= 1
    print(l)


def merge_sort(l):

    if len(l) == 1:
        return l
    else:
        median = len(l)//2
        left_half = merge_sort(l[:median])
        right_half = merge_sort(l[median:])
        return merge(left_half, right_half)


def merge(left, right):

    m = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            m.append(left[i])
            i += 1
        else:
            m.append(right[j])
            j += 1

    m.extend(right[j:])
    m.extend(left[i:])

    return m

def quick_sort(a, l, r):
    l = partition(a, 0)
    while l < r:
        quick_sort(a, )



def partition(a, l):
    p = len(a) - 1
    r = len(a) - 2

    while l < r:

        while a[l] <= a[p] or a[r] > a[p]:
            l += 1
            r -= 1

        if l < r:
            a[l], a[r] = a[r], a[l]


    a[l], a[p] = a[p], a[l]
    return l


if __name__ == "__main__":
    myList = [5, 8, 4, 0, 6, 9, 1]
    arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
    # bubble_sort(myList)
    # selection_sort(arr)
    # insertion_sort(arr)
    # print(merge(myList, arr))
    # print(f'merge sort array is {merge_sort(myList)}')
    print(f'quick sort array is {quick_sort(myList, 0)}')
