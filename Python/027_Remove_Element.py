class Solution(object):
    def removeElement(self, nums, val):
        k = 0

        for v in nums:
            if v != val:
                nums[k] = v
                k += 1
        return k

