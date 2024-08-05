class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq_map = {}
        distinct_arr = []
        
        # Count the frequency of each element
        for item in arr:
            freq_map[item] = freq_map.get(item, 0) + 1
        
        # Create a list of distinct elements
        for item in arr:
            if freq_map[item] == 1:
                distinct_arr.append(item)
        
        # Check if k is within bounds
        if 0 < k <= len(distinct_arr):
            return distinct_arr[k - 1]
        else:
            return ""