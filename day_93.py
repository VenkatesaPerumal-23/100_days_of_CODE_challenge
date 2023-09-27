#Largest Odd Number in String
class Solution:
    def largestOddNumber(self, num: str) -> str:
        length=len(num)-1
        for i in range(length,-1,-1):
            if(int(num[i])%2!=0):
                return num[0:i+1] 
            
        return ""