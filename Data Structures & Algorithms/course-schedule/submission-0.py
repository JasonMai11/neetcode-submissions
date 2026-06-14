class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        dic = defaultdict(list)

        for c, p in prerequisites:
            dic[c].append(p)
            
        seen = set()

        def dfs(crs):
            if crs in seen:
                return False
            if dic[crs] == []:
                return True
            seen.add(crs)
            for pre in dic[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            dic[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True