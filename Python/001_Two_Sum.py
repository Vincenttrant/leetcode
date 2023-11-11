class Solution(object):
    def twoSum(self, nums, target):
        hash = {}

        for i, v in enumerate(nums):
            difference = target - v
            if difference in hash:
                return [i, hash[difference]]
            hash[v] = i
        print(hash)