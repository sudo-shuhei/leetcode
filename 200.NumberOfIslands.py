class Solution: #深さ優先探索
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        if len(grid) == 0:
            return 0
        self.lenx = len(grid[0])
        self.leny = len(grid)
        print(self.lenx,self.leny)

        result = 0
        for y in range(self.leny):
            for x in range(self.lenx):
                if grid[y][x] == "1":
                    self.DFS(x,y)
                    result += 1

        print(result)
        return result

    def DFS(self, x, y):
        #今の位置を0に変える
        self.grid[y][x] = "0"

        #上下左右が1なら0に変え、再帰呼び出しする
        if x+1 < self.lenx:
            if self.grid[y][x+1] == "1":
                self.grid[y][x+1] = "0"
                self.DFS(x+1, y)
        if x-1 >= 0:
            if self.grid[y][x-1] == "1":
                self.grid[y][x-1] = "0"
                self.DFS(x-1, y)
        if y+1 < self.leny:
            if self.grid[y+1][x] == "1":
                self.grid[y+1][x] = "0"
                self.DFS(x, y+1)
        if y-1 >=0:
            if self.grid[y-1][x] == "1":
                self.grid[y-1][x] = "0"
                self.DFS(x, y-1)
