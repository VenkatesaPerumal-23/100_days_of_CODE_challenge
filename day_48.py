#remove duplicates from sorted array
class Solution(object):
    def removeDuplicates(self, nums):
        num_set=set(nums)
        num_list=list(num_set)
        num_list.sort()
        k=0
        for j in range(len(num_list)):
            nums[j]=num_list[j] 
            k+=1
        return k