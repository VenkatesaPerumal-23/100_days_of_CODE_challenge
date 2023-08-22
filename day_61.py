#majority element
class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        nums_set=set(nums)
        dict_val={}
        for i in nums_set:
            count=nums.count(i) 
            dict_val[i]=count 
        keys=list(dict_val.keys())
        values=list(dict_val.values()) 
        max_count=values.index(max(values)) 
        return keys[max_count]