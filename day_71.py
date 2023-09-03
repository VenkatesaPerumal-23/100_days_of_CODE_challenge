#longest subarray with sum k

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        dictmap={} 
        maxlen=0 
        summ=0 
        for i in range(n):
            summ+=arr[i] 
            
            if summ==k:
                maxlen=max(maxlen,i+1)
                
            rem=summ-k 
            if rem in dictmap:
                length=i-dictmap[rem] 
                maxlen=max(maxlen,length) 
                
            if summ not in dictmap:
                dictmap[summ]=i 
                
        return maxlen