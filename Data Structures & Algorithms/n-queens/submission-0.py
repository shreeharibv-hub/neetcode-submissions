class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path = []
        for i in range(n):
            path.append(["."] * n)
        res=[]
        cols=set()
        dio1=set()
        dio2=set()

        def backtrack(row,path):
            if row==n:
                res.append(["".join(r) for r in path])
                return
            if row>n:
                return
            
            for col in range(n):
                if col not in cols and row-col not in dio1 and row+col not in dio2:
                    path[row][col]="Q"
                    cols.add(col)
                    dio1.add(row-col)
                    dio2.add(row+col)
                    backtrack(row+1,path)
                    path[row][col]="."
                    cols.remove(col)
                    dio1.remove(row-col)
                    dio2.remove(row+col)



        backtrack(0,path)
        return res

        