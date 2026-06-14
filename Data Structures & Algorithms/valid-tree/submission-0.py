class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        from collections import defaultdict
        
        graph = defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        seen = set()
        
        def dfs(i, prev):
            if i in seen:
                return False
            seen.add(i)
            for j in graph[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, -1) and n == len(seen)