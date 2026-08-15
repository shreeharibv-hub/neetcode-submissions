class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            if x.lstrip("-").isdigit():
                stack.append(int(x))

            elif x in '+-/*':
                val1=stack.pop()
                val2=stack.pop()
                if x == "+":
                    val3 = val2 + val1
                elif x == "-":
                    val3 = val2 - val1
                elif x == "*":
                    val3 = val2 * val1
                elif x == "/":
                    val3 = int(val2 / val1)
                stack.append(int(val3))

        return stack[-1]


        