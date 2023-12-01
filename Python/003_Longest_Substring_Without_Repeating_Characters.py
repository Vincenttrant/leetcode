class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l, r, output = 0, 0, 0
        substring = ""
        while r < len(s):
            while s[r] in substring:
                l += 1
                substring = s[l:r]
            r += 1
            substring = s[l:r]
            output = max(output, len(substring))
        return output

