from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        route = []
        x, y = rStart, cStart
        route.append([x, y])
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 0
        d = 0
        
        while len(route) < rows * cols:
            if d == 0 or d == 2:
                steps += 1
            
            for _ in range(steps):
                x += directions[d][0]
                y += directions[d][1]
                
                if 0 <= x < rows and 0 <= y < cols:
                    route.append([x, y])
            
            d = (d + 1) % 4
        
        return route