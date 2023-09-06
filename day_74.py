#threeSum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sum_list=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1 
            k=len(nums)-1 

            while(j<k):
                summ=nums[i]+nums[j]+nums[k]
                if summ>0:
                    k-=1 
                elif summ<0:
                    j+=1 
                else:
                    list=[nums[i],nums[j],nums[k]]
                    sum_list.append(list)
                    j+=1 
                    k-=1 
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1 
                    while(j<k and nums[k]==nums[k+1]):
                        k-=1 
        return sum_list