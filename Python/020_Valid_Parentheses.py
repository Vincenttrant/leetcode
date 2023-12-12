class Solution(object):
    def isValid(self, s):
        parentheses = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for c in s:
            if c in parentheses:
                stack.append(c)
            elif not stack or parentheses[stack.pop()] != c:
                return False
        return not stack 