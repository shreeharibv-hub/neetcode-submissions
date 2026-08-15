class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for x in s:
            if x in ")}]":
                if not stack:
                    return False
                if stack[-1]=='(' and x==')' or stack[-1]=='[' and x==']'or stack[-1]=='{' and x=='}':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)

                
        if not stack:
            return True
        return False