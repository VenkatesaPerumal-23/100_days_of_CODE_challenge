#rotate the array by k steps
class Solution(object):
    def rotate(self, nums, k): 
        length_of_array=len(nums) 
        slice_index=k%length_of_array 
        first_slice=nums[-slice_index:]
        nums[slice_index:]=nums[:-slice_index] 
        nums[:slice_index]=first_slice