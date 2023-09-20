#Number of occurrence
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index_arr=[] 
        first_index=-1
        second_index=-1 
        low=0
        high=len(nums)-1 
        while(low<=high):
            mid=(low+high)//2 
            if(nums[mid]==target):
                first_index=mid 
                high=mid-1 
            elif(nums[mid]>target):
                high=mid-1
            else:
                low=mid+1 
        index_arr.append(first_index)
        
        low=0 
        high=len(nums)-1 
        while(low<=high):
            mid=(low+high)//2 
            if(nums[mid]==target):  
                second_index=mid 
                low=mid+1
            elif(nums[mid]>target):
                high=mid-1 
            else:
                low=mid+1  
        index_arr.append(second_index) 
        return index_arr