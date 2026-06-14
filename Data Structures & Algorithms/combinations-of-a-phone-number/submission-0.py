class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if digits == '':
            return []

        res = []

        def backtrack(i, ret):
            if i == len(digits):
                res.append(ret)
                return

            digit = digits[i]
            for c in dic[digit]:
                backtrack(i + 1, ret + c)
        
        backtrack(0, '')
        return res