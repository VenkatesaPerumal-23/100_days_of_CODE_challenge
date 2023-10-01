#Sort Characters By Frequency
class Solution:
    def frequencySort(self, s: str) -> str:
        HashMap={} 
        for i in s:
            if(i not in HashMap):
                HashMap[i]=1 
            else:
                HashMap[i]+=1 
        res_str=""      
        for char in sorted(HashMap.items(),key=lambda x:x[1]):
            res_str+=char[0]*char[1] 
        return res_str[::-1]