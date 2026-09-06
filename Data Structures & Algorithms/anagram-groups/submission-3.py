class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            sortedStr = ''.join(sorted(i))
            hashmap[sortedStr].append(i)
        return list(hashmap.values())
            