class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        l = 0
        ret = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            ret = max(ret, r - l + 1)

        return ret