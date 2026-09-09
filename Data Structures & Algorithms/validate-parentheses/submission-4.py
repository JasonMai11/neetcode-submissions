class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(',
                '}': '{',
                ']': '['
                }

        for i in s:
            if not stack and i in dic:
                return False
            else:
                if i not in dic:
                    stack.append(i)
                elif i in dic and stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
        return False if stack else True