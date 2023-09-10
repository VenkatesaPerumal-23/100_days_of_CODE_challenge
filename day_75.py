#fourSum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        four_sum_list=[] 
        summ=0
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue 

            for j in range(i+1,len(nums)):
                    if(j!=i+1 and nums[j]==nums[j-1]):
                        continue 

                    k=j+1 
                    l=len(nums)-1 
                    while(k<l):

                        summ=nums[i];
                        summ+=nums[j];
                        summ+=nums[k];
                        summ+=nums[l];
                        if(summ==target):
                            list=[nums[i],nums[j],nums[k],nums[l]];
                            four_sum_list.append(list)
                            k+=1 
                            l-=1 
                            while(k<l and nums[k]==nums[k-1]):
                                k+=1
                            while(k<l and nums[l]==nums[l+1]):
                                l-=1

                        elif(summ<target):
                            k+=1
                        else: 
                            l-=1 
        return four_sum_list
