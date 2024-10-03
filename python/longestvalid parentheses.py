from collections import deque

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = deque()
        stack.append(-1)  # Initialize with -1 to represent the base index

        max_len = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:  # s[i] == ")"
                stack.pop()
                if not stack:  # If the stack is empty, push the current index
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
s=Solution()
string="((())"
validlength=s.longestValidParentheses(string)
print(validlength)