class Solution(object):
    def subsetsWithDup(self, nums):
        n, result = len(nums), []
        def powerSet(nums, i, subset):
            if i == n:
                subset.sort()
                if subset not in result:
                    result.append(subset)
                return
            powerSet(nums, i+1, subset)
            powerSet(nums, i+1, subset + [nums[i]])
        powerSet(nums, 0, [])
        return result