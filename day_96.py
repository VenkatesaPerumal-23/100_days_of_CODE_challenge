#Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #Using HashMap ie:dict
        map_st={}
        map_ts={} 
        for i in range(len(s)):
            x1,y1=s[i],t[i] 
            
            if(x1 in map_st and map_st[x1]!=y1) or (y1 in map_ts and map_ts[y1]!=x1):
                return False
                  
            map_st[x1]=y1 
            map_ts[y1]=x1
        return True