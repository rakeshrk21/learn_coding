def permute(nums):
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])  # found one full permutation
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])

            backtrack(path, used)  # recursive step

            # backtrack
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result

print(permute([1, 9, 7, 8]))
print([False] * 4)
