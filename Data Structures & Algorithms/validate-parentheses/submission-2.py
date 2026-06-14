class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []

        for i in s:
            if i in dic and stack:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if stack:
            return False
        return True