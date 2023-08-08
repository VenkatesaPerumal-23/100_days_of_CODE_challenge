#checking array is sorted and rotated
class Solution(object):
    def check(self, nums):
        sorted_list=sorted(nums) 
        for i in range(len(nums)):
            if(nums[i:]+nums[:i]==sorted_list):
                return True 
        return False