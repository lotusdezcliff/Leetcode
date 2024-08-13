class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtrack(candidates, 0, target, [], res)
        return res

    def backtrack(self, candidates, start, target, path, res):
        if target < 0:
            return
        elif target == 0:
            res.append(path[:])
        else:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                self.backtrack(candidates, i + 1, target - candidates[i], path, res)
                path.pop()






        