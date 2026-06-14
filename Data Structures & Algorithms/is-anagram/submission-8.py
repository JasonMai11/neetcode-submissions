class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        counterS = Counter(s)
        counterT = Counter(t)

        if len(s) != len(t):
            return False

        for i in s:
            if i not in counterT:
                return False
            else:
                counterT[i] -= 1
                if counterT[i] < 0:
                    return False

        return True