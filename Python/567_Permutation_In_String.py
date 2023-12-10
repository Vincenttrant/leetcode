class Solution(object):
    def checkInclusion(self, s1, s2):
        hash, hash2 = {}, {}
        l, r = 0, 0

        for i in range(len(s1)):
            hash[s1[i]] = 1 + hash.get(s1[i], 0)

        while r < len(s2):
            hash2[s2[r]] = 1 + hash2.get(s2[r], 0)

            if (r - l) == len(s1):
                hash2[s2[l]] -= 1
                if hash2[s2[l]] == 0:
                    del hash2[s2[l]]
                l += 1

            r += 1

            if hash == hash2:
                return True
        return False