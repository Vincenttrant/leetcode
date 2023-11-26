class Solution(object):
    def longestConsecutive(self, nums):
        count = 0
        newNums = set(nums)

        for i in newNums:
            if (i - 1) not in newNums:
                curCount = 0
                while (i + curCount) in newNums:
                    curCount += 1
                count = max(count, curCount)
        return count

