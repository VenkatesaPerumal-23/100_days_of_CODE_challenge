#missing_and_repeating_numbers
class Solution:
    def findTwoElement( self,arr, n): 
        m1=n*(n+1)//2 
        m2=(n*(n+1)*(2*n+1))//6 
        
        s1=0
        s2=0 
        for i in range(n):
            s1+=arr[i] 
            s2+=arr[i]*arr[i] 
            
        val1=s1-m1 
        val2=s2-m2 
        val2=val2//val1 
        
        x=(val1+val2)//2 
        y=x-val1 
        
        return [x,y]