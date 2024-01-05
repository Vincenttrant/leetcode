class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            rock1, rock2 = heapq.heappop(stones), heapq.heappop(stones)

            if rock1 != rock2:
                heapq.heappush(stones, -abs(rock1 - rock2))

        if not stones:
            return 0
        return -stones[0]