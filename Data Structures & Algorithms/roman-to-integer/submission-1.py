class Solution:
    def romanToInt(self, s: str) -> int:
        
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        max_right = 0

        for char in reversed(s):
            value = values[char]

            if value < max_right:
                result -= value
            else:
                result += value
                max_right = value

        return result