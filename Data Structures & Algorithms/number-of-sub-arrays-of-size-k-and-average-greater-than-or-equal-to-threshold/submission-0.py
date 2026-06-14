class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res, l = 0, 0
        acc = sum(arr[:k])

        for r in range(k, len(arr)):
            if acc/k >= threshold:
                res += 1
            acc -= arr[l]
            acc += arr[r]
            l += 1
        if acc/k >= threshold:
            res += 1
        return res



            