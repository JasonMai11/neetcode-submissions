from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            t = ''.join(sorted(s))
            
            if t in dic:
                dic[t].append(s)
            else:
                dic[t] = [s]
        ret = []

        for i in dic:
            ret.append(dic[i])
        return ret
                