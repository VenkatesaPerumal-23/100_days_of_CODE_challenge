#Merge intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length=len(intervals) 
        intervals.sort() 
        ans_list=[]
        for i in range(length):
            if not ans_list or intervals[i][0]>ans_list[-1][1]:
                ans_list.append(intervals[i]) 
            else:
                ans_list[-1][1]=max(ans_list[-1][1],intervals[i][1]) 
        return ans_list