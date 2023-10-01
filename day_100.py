#Maximum Nesting Depth of the Parentheses
class Solution:
    def maxDepth(self, s: str) -> int:
        curr_max=0 
        res_max=0 
        for i in range(len(s)):
            if (s[i] == '('):
                curr_max+=1 
                if(curr_max>res_max):
                    res_max=curr_max 
                    
            elif (s[i] == ')'):
                if(curr_max>0):
                    curr_max-=1 
                else:
                    return -1 
        if(curr_max!=0):
            return -1 
        return res_max