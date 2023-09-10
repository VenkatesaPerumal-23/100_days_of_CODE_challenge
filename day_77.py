#Count the Number of Beautiful Subarrays
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        xor=0 
        count=0 
        dict=Counter({0:1})
        for i in range(len(nums)):
            xor=xor^nums[i]  
            count+=dict[xor] 
            dict[xor]+=1 
        return count