#Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]: 
        pascal_list=[] 
        for each in range(1,numRows+1):
            temp_list=[]
            for i in range(1,each+1): 
                temp_list.append(self.ncr(each-1,i-1))
            pascal_list.append(temp_list)   
            
        return pascal_list
    
    
    def ncr(self,numRows,r):
        pascal=1 
        for i in range(r):
            pascal=pascal*(numRows-i) 
            pascal//=(i+1) 
        return pascal