#longest consecutive sequence 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        num_set=set(nums)
        long_count= -0 
        for i in nums:
            if (i-1) not in num_set:
                length=0 
                while(i+length) in num_set:
                    length+=1 
                long_count=max(length,long_count)
        return long_count