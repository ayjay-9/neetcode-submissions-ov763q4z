class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize the crs: prerequisite map
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()
        finished = set()
        order = []
        def dfs(crs):
            if crs in visit:
                return False
            if crs in finished:
                return True

            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            finished.add(crs)
            order.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []
        return list(order)