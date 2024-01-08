class Solution(object):
    def kClosest(self, points, k):
        distances = []

        for x, y in points:
            distance = math.sqrt(((x - 0) ** 2) + ((y - 0) ** 2))
            distances.append([distance, x, y])

        heapq.heapify(distances)
        output = []

        for i in range(k):
            distance, x, y = heapq.heappop(distances)
            output.append([x, y])

        return output