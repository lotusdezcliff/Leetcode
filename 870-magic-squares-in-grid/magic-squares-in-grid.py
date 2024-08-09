class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # row == grid.length
        # col == grid[i].length
        # 1 <= row, col <= 10
        # 0 <= grid[i][j] <= 15
        result = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(len(grid)):
            if col != len(grid[i]):
                return 0
        
        # Case that cannot form 3x3 suqare
        if row <= 2 or col <= 2:
            return 0
        
        # Start from (1,1) ... to (row-2, col-2)
        #    (i,j) (i,j+1) (i,j+2)
        # (i+1,j) (i+1,j+1) (i+1,j+2)
        # (i+2,j) (i+2,j+1) (i+2,j+2)
        for i in range(row - 2):
            for j in range(col - 2):
                num_list = [grid[i][j], grid[i][j+1], grid[i][j+2], grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]
                if sorted(num_list) != list(range(1, 10)):
                    continue
                sum_Ldia = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                sum_Rdia = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
                sum_r1 = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                sum_r2 = grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2]
                sum_r3 = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                sum_c1 = grid[i][j] + grid[i+1][j] + grid[i+2][j]
                sum_c2 = grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1]
                sum_c3 = grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2]
                sum_list = [sum_Ldia, sum_Rdia, sum_r1, sum_r2, sum_r3, sum_c1, sum_c2, sum_c3]
                if (sum_Ldia == sum_Rdia == sum_r1 == sum_r2 == sum_r3 == sum_c1 == sum_c2 == sum_c3):
                    result += 1
        return result
                        
                        