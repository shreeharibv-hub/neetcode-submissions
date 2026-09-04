class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        open_=0
        close=0
        def backtrack(path):
            nonlocal open_,close
            if open_==n and close==n:
                res.append(''.join(path))
                return

            if open_<n:
                path.append('(')
               
                open_+=1
                backtrack(path)
                path.pop()
                open_-=1
                
            if close<open_:
                path.append(')')
                close+=1
                backtrack(path)
                path.pop()
                close-=1

        backtrack([])
        return res


