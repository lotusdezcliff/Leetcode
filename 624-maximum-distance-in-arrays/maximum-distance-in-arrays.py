class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        overall_min = arrays[0][0]
        overall_max = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            max_distance = max(max_distance, abs(current_max - overall_min), abs(overall_max - current_min))
            
            overall_min = min(overall_min, current_min)
            overall_max = max(overall_max, current_max)
        
        return max_distance