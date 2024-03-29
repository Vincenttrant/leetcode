class Solution(object):
    def findKthLargest(self, nums, k):
        nums = [-i for i in nums]
        heapq.heapify(nums)

        for i in range(k - 1):
            heapq.heappop(nums)

        return -nums[0]