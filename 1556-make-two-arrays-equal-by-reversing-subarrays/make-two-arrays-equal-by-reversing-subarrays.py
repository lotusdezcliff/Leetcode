class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if sorted(arr) == sorted(target):
            return True
        else:
            return False