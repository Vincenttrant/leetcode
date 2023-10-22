class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        hash1, hash2 = {}, {}

        for i in range(len(s)):
            hash1[s[i]] = 1 + hash1.get(s[i], 0)
            hash2[t[i]] = 1 + hash2.get(t[i], 0)
        
        if hash1 == hash2:
            return True
        return False