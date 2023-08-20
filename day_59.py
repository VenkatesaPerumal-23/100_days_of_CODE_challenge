#twosum
class Solution(object):
    def twoSum(self, nums, target):
      length=len(nums) 
      for i in range(length):
            for j in range(i+1,length):
                if(nums[j]==target-nums[i]):
                    return [i,j]