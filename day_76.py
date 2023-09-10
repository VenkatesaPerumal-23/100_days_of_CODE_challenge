#Largest subarray with 0 sum
class Solution:
    def maxLen(self, n, arr):
       dicti={} 
       summ=0 
       maximum=0 
       for i in range(n):
           summ+=arr[i]
           if summ==0:
               maximum=i+1 
               
           else:
               if summ in dicti:
                   maximum=max(maximum,i-dicti[summ]) 
                
               else:
                   dicti[summ]=i
       return maximum
