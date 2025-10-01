class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        def bfs(r,c):
            search_queue = deque()
            visit.add((r,c))
            search_queue.append((r,c))

            while search_queue:
                row, col = search_queue.popleft()
                directions = [[1,0], [-1,0], [0,1],[0,-1]]

                for dr,dc in directions:
                    r,c =  row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r,c) not in visit):
                        search_queue.append((r,c))
                        visit.add((r,c))
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visit= set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    count+= 1
        return(count)