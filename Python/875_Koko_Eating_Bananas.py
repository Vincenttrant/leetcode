class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        result = max(piles)

        while l <= r:
            k = (l + r) // 2
            count = 0

            for i in piles:
                count += i // k
                if i % k != 0:
                    count += 1
            if count <= h:
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1

        return result