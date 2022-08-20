
def sum_to_target_bf(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# time complexity o(n^2)  space complexity o(1)


def sum_to_target_1(nums, target):
    map = dict()
    for i in range(len(nums)):
        temp = target - nums[i]
        # if the temp exists in the map, then that number exists
        if temp in map:
            return [i, map[temp]]
        # if the temp does not exists in the map, then that add the number and the index in the map
        else:
            map[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    nums1 = [4, -2, 5, 0, 6, 3, 2, 7]
    target1 = 1
    print("brute force", sum_to_target_bf(nums, target))
    print("smarter approach", sum_to_target_1(nums, target))
    print('=' * 20)
    print("smarter approach", sum_to_target_1(nums1, target1))
    print("brute force", sum_to_target_bf(nums1, target1))
