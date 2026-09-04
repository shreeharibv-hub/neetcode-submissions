class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates=sorted(candidates)
        def backtrack(i,path,remain):
            if remain==0:
                if path not in res:
                    res.append(path.copy())
                    return
            if remain<0:
                return

            if i==len(candidates):
                return

            path.append(candidates[i])
            backtrack(i+1,path,remain-candidates[i])
            path.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1,path,remain)
        backtrack(0,[],target)
        return res
        