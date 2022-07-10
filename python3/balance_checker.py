class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        if len(x)<2:
            return False;
        stack=[]
        d={
            "{":"}",
            "(":")",
            "[":"]"
        }
        for s in x:
            if s in "{([":
                stack.append(s)
            else:
                if len(stack)<1:
                    return False
                elif d[stack[-1]]==s:
                    stack.pop()
                else:
                    return False
            # print(stack,s)
        if len(stack)>0:
            return False
        else:
            return True
    
    
