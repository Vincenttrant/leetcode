class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:
            output = numbers[l] + numbers[r]
            if output == target:
                return [l + 1, r + 1]
            elif output < target:
                l += 1
            else:
                r -= 1