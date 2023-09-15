#Reverse Pairs
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count=self.mergeSort(nums,0,len(nums)-1)
        return count

    def mergeSort(self,nums,low,high):
        count = 0
        if low>=high:
            return count
        mid = (low+high)//2
        count+=self.mergeSort(nums,low,mid)
        count+=self.mergeSort(nums,mid+1,high)
        count+=self.countPairs(nums,low,mid,high)
        self.merge(nums,low,mid,high)
        return count
    

    def countPairs(self,nums,low,mid,high):
        count = 0
        left = low
        right = mid+1

        while left<=mid and right<=high :
            if  nums[left]>2*nums[right]:
                count += (mid-left)+1
                right+=1
            else:
                left+=1
        
        return count


    def merge(self,nums,low,mid,high):
        temp = []
        left = low
        right = mid+1

        while left<=mid and right<=high:
            if nums[left]<= nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while left<=mid:
            temp.append(nums[left])
            left+=1
        while right<=high:
            temp.append(nums[right])
            right+=1

        for i in range(low,high+1):
            nums[i]=temp[i-low] 