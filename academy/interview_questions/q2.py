# write a program to find all pairs of integers whose sum is equal to a given number e.g 9 -> [6,3)

nums = [2, 6, 3, 9, 11]
nums.sort()
print(nums)
target = 11
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            continue
        elif nums[i] + nums[j] == target:
            print(nums[i], nums[j])




# pseudo code

