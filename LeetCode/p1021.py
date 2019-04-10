# Original Solution.
class Solution1(object):
    def removeOuterParentheses(self, S: str) -> str:
        s = []
        openp = 0
        start = 0

        # Create functional decompositions. Store in s.
        for i in range(len(S)):
            if S[i] == '(':
                openp += 1
            else:
                openp -= 1

            if openp == 0:
                s.append(S[start:i + 1])
                start = i + 1
        
        # Remove outer parentheses and construct output string.
        clean = ""
        for string in s:
            clean += string[1:-1]
        
        return clean

# Cleaned up solution. Inspired by https://leetcode.com/problems/remove-outermost-parentheses/discuss/270022/JavaC%2B%2BPython-Count-Opened-Parenthesis
class Solution2(object):
    def removeOuterParentheses(self, S: str) -> str:
        output = ""
        p = 0
        for c in S:
            p += 1 if c == '(' else -1
            if (p > 1 and c == '(') or (p > 0 and c == ')'):
                output += c
        return output

sol = Solution2()
print(sol.removeOuterParentheses("(()())(())"))
print(sol.removeOuterParentheses("(()())(())(()(()))"))
print(sol.removeOuterParentheses("()()"))