class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}       
        if not digits:
            return []
        res=[]
        def backtrack(i,path):
            
            if len(path)==len(digits):
                res.append(''.join(path))
            if i==len(digits):
                return
            for leter in phone[digits[i]]:
                path.append(leter)
                backtrack(i+1,path)
                path.pop()

        backtrack(0,[])
        return res
            