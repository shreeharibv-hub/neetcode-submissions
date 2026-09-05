class Solution:
    def exist(self, board, word):
        used = set()

        def backtrack(k, i, j, path):
            if (i,j) in used :
                return False
            if k>len(word):
                return False
            if k==len(word):
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
                return False
            if board[i][j]!=word[k]:
                return False
            path.append(board[i][j])
            used.add((i,j))
            
            up=backtrack(k+1,i-1,j,path)
            down=backtrack(k+1,i+1,j,path)
            left=backtrack(k+1,i,j-1,path)
            right=backtrack(k+1,i,j+1,path)
             
            if up or down or left or right:
                return True
            
            path.pop()
            used.remove((i,j))
            return False
        for i in range(len(board)):
            for j in range (len(board[0])):
                if backtrack(0,i,j,[]):
                    return True
        return False
