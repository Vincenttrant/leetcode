class Solution(object):
    def maxArea(self, height):
        output = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            output = max(area, output)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return output