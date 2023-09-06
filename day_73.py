#Majority Element II
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dicts=dict(Counter(nums))
        list=[]
        n=len(nums)//3
        for key,value in dicts.items():
            if value>n:
                list.append(key) 
        return list
                    