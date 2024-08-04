from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        subarray_sums = []
        
        # Generate all subarray sums
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
        
        # Sort the subarray sums
        subarray_sums.sort()
        
        # Calculate the sum of elements from index `left-1` to `right-1` (inclusive)
        result = sum(subarray_sums[left-1:right]) % MOD
        
        return result

# Example usage:
solution = Solution()
nums = [1, 2, 3, 4]
n = len(nums)
left = 3
right = 6
print(solution.rangeSum(nums, n, left, right))  # Output should be the sum of the 3rd to 6th smallest subarray sums modulo 10^9 + 7