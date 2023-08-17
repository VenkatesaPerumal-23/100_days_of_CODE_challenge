#find that one
class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        
        xor_op=0 
        for i in nums:
            xor_op=xor_op^i     
        return xor_op