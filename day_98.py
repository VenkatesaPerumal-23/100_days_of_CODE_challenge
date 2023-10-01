#Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort and compare each character 
        if(len(s)!=len(t)):
            return False 
        sort_s=sorted(s)
        sort_t=sorted(t)  
        for i in range(len(sort_s)):
            if(sort_s[i]!=sort_t[i]):
                return False 
            
        return True