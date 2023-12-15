class Solution(object):
    def carFleet(self, target, position, speed):
        pair = sorted(zip(position, speed))
        stack = []

        for p, s in pair[::-1]:
            stack.append(float((target - p)) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return(len(stack))