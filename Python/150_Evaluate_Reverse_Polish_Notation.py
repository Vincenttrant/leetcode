class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                val1, val2 = stack.pop(), stack.pop()
                if c == "+":
                    stack.append(val1 + val2)
                elif c == "-":
                    stack.append(val2 - val1)
                elif c == "*":
                    stack.append(val1 * val2)
                elif c == "/":
                    stack.append(int(float(val2) / val1))

        return stack[0]