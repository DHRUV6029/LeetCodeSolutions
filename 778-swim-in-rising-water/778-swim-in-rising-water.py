class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        row = len(grid)
        col = len(grid[0])

        q = [[grid[0][0], 0 , 0]]
        visited = set()
        visited.add((0, 0))

        while q:
            for x in range(0, len(q)):
                cur, r, c = heapq.heappop(q)

                #end condition
                if r == row-1 and c==col-1:
                    return(cur)

                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if nr<0 or nr>row-1 or nc<0 or nc>col-1 or (nr,nc) in visited:
                        continue
                    visited.add((nr, nc))
                    heapq.heappush(q, [max(cur , grid[nr][nc]), nr, nc])