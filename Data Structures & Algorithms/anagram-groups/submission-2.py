class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            sortedStr = ''.join(sorted(i))
            if sortedStr in hashmap:
                hashmap[sortedStr].append(i)
            else:
                hashmap[sortedStr] = [i]
        return list(hashmap.values())
            