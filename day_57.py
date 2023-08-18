#subarray sum equals to k
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: 
        map={0:1} 
        count=0 
        presum=0 
        for x in nums:
            presum+=x 
            if(presum-k) in map:
                count+=map[presum-k] 
            if presum in map:
                map[presum]+=1 
            else:
                map[presum]=1 
                
        return count