class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        
        for c in tokens:
            if c not in ["+", "-", "*", "/"]:
                stack.append(c)
            else:
                a=int(stack.pop())
                b=int(stack.pop())
                
                if c=="+":
                    stack.append(a+b)
                elif c=="-":
                    stack.append(b-a)
                elif c=="*":
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
        
        return stack.pop()
        