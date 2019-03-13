class Solution(object):
    def isValid(self, s):
        stack = []
        opens = set(["(", "[", "{"])
        pairs = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != pairs[c]:
                    return False
                stack.pop()
        return len(stack) == 0

sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))