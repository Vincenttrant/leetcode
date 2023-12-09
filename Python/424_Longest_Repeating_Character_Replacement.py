class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        result = 0
        hash = {}

        for r in range(len(s)):
            hash[s[r]] = 1 + hash.get(s[r], 0)

            while (r - l + 1) - max(hash.values()) > k:
                hash[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result