class Solution(object):
    def combinationSum(self, candidates, target):

        ans = []

        def dfs(cur, total, idx):
            if total > target:
                return
            if total == target:
                ans.append(cur)
                return
            for i in range(idx, len(candidates)):
                dfs(cur + [candidates[i]], total + candidates[i], i)

        dfs([], 0, 0)
        return ans