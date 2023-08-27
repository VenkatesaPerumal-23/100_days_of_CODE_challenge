#Rearrange Array Elements by Sign
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        mod_list=[0]*n 
        pos_index,neg_index=0,1 
        for i in range(n):
            if nums[i]>0:
                mod_list[pos_index]=nums[i]
                pos_index+=2 
            else:
                mod_list[neg_index]=nums[i]
                neg_index+=2 
        return mod_list