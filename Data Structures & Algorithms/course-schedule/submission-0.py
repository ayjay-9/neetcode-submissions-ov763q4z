class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit: # Cycle detected
                return False
            if preMap[crs] == []: # Course has no prerequisites and can be completed
                return True

            visit.add(crs) # Since it's not already there
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs) # Avoid visiting same one again
            preMap[crs] = [] # Course can be completed
            return True # So return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True