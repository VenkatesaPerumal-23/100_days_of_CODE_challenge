class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: 
        count=0 
        max_list=[]
        for i in nums: 
            if(i==1):
                count+=1  
                max_list.append(count)
            else:
                count=0  
                max_list.append(count)
        return max(max_list)