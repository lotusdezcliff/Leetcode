class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = nums[0]
        for i in range(len(nums) - 1):
            if abs(nums[i + 1]) < abs(res):
                res = nums[i + 1]
            elif abs(nums[i + 1]) == abs(res):
                res = max(nums[i + 1], res)
        return res
