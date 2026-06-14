class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        l = 0
        res = 0
        max_f = 0

        for r in range(len(s)):
            char = s[r]
            if char not in freq_map:
                freq_map[char] = 1
            elif char in freq_map:
                freq_map[char] += 1

            max_f = max(max_f, freq_map[char])

            while (r - l + 1) - max_f > k:
                freq_map[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
