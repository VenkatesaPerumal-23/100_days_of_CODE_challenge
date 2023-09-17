#Return Max_Product
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=float('-inf') 
        pre=1
        suff=1 
        for i in range(len(nums)):
            if(pre==0):
                pre=1 
            if(suff==0):
                suff=1 
            pre=pre*nums[i] 
            suff=suff*nums[len(nums)-i-1]
            max_prod=max(max_prod,max(pre,suff)) 
        return max_prod