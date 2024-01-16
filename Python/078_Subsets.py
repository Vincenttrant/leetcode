class Solution(object):
    def subsets(self, nums):
        n, result = len(nums), []
        def powerSet(nums, i, subSet):
            if i==n:
                result.append(subSet)
                print(subSet)
                return
            powerSet(nums, i+1, subSet)
            powerSet(nums, i+1, subSet + [nums[i]])
        powerSet(nums, 0, [])
        return result