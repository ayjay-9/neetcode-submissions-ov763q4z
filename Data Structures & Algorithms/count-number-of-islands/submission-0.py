class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r: int,c: int):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft() # pop() for DFS solution
                directions = [[1,0], [-1,0], [0,1], [0,-1]] # [[Right], [Left], [Up], [Down]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r=r, c=c)
                    islands += 1
        return islands