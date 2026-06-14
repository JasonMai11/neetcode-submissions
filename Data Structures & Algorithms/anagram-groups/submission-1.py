class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        hashmap = defaultdict(list)
        for s in strs:
            k = sorted(s)
            key = "".join(k)
            hashmap[key].append(s)

        res = []
        for k in hashmap:
            res.append(hashmap[k])
        return res
