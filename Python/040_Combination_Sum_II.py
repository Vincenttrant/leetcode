class Solution(object):
    def combinationSum2(self, candidates, target):
        def recurse(start, comboSum, combo):
            if comboSum == target:
                res.append(combo[::])

            for i in range(start, len(candidates)):
                if comboSum+candidates[i] <= target:
                    if i != start and candidates[i] == candidates[i-1]:
                        continue
                    combo.append(candidates[i])
                    recurse(i+1, comboSum+candidates[i], combo)
                    combo.pop()
            return res

        res = []
        candidates.sort()
        return recurse(0, 0, [])