#Rotate String
class Solution:
    def rotateString(self, s: str, goal: str) -> bool: 
        for i in range(len(s)):
            if(i==len(s)-1):
                if(s[i:]+s[:i] == goal):
                    return True
            if(len(s)==0):
                return True
            if(len(s) != len(goal)):
                return False
            
            else:
                left=s[0:i+1]
                right=s[i+1:]+left
                if(right==goal):
                    return True
        return False