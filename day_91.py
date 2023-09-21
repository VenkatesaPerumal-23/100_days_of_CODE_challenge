#find K Rotation in Rotated Sorted Array
class Solution:
    def findKRotation(self,arr, n):
        low=0 
        high=n-1 
        index=-1
        ans=float('inf')
        while(low<=high):
            mid=(low+high)//2 
            if(arr[low]<=arr[high]):
                if(arr[low]<ans):
                    index=low 
                    ans=min(ans,arr[low])
                    break
                
            if(arr[low]<=arr[mid]):
                if(arr[low]<ans):
                    index=low  
                    ans=min(ans,arr[low])
                low=mid+1
            else:
                if(arr[mid]<ans):
                    index=mid 
                    ans=min(ans,arr[mid])
                high=mid-1 
                    
        return index