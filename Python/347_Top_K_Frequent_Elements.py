class Solution(object):
    def topKFrequent(self, nums, k):
        table = {}
        tableList = []

        for i in nums:
            table[i] = 1  + table.get(i, 0)

        tableList = list(table.items())
        tableList.sort(key=lambda x: x[1], reverse=True)
        
        res = []

        for n in tableList:
            res.append(n[0])
            if len(res) == k:
                return res