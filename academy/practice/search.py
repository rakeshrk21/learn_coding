def binary_search(nums, target):
    nums.sort()

    left = 0
    right = len(nums) -1

    while left<=right:
        mid = (left + (right - left))//2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid -1
        else:
            left = mid + 1

    return -1


if __name__ == "__main__":
    print(binary_search([8, 6,  9 ,78, 92, 3, 67, 45, 89], 3))
