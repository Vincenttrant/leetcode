class Solution(object):
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                index, temp = stack.pop()
                result[index] = i - index
            stack.append([i, t])
        return result
