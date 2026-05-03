class Solution:
    def largestUniqueNumber(self, nums):
        unique = dict()
        l = []
        
        for num in nums:
            if num in unique:
                unique[num] += 1
            else:
                unique[num] = 1

        for key in unique:
            if unique[key] == 1:
                l.append(key)
        
        if(len(l)<1):
            return -1
        else:
            return max(l)