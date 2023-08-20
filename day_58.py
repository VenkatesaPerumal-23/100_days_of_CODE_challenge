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
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends