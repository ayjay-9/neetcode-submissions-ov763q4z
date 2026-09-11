class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        
        conMap = {i: [] for i in range(n)}
        for ai, bi in edges:
            conMap[ai].append(bi)
            conMap[bi].append(ai)
        visit = set()

        def dfs(ai):
            if ai in visit:
                return
            
            visit.add(ai)
            for bi in conMap[ai]:
                dfs(bi)

        count = 0
        for ai in range(n):
            if ai not in visit:
                count += 1
                dfs(ai)
        return count