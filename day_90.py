#Minimum element in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0 
        high=len(nums)-1 
        min_element=float('inf')
        while(low<=high):
            mid=(low+high)//2 
            if(nums[low]<=nums[mid]):
                min_element=min(min_element,nums[low])
                low=mid+1 
            else:
                min_element=min(min_element,nums[mid]) 
                high=mid-1 
        return min_element