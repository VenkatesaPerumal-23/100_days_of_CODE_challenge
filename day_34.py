#prime number
import math
class Solution:
    def isPrime(self,N):
       if(N==1):
           return 0 
       if(N==2):
           return 1 
           
       sqrtval=math.sqrt(N)+1
       sqrtval=int(sqrtval)
       for i in range(2,sqrtval):
           if(N%i==0):
               return 0 
               
       return 1     
         
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends

#reverse integer
class Solution:
    def reverse(self, x: int) -> int:
        max=pow(2,31) - 1 
        max=int(max) 
        min=pow(-2,31)
        min=int(min)

        res=0  
        while x:
            rem=int(math.fmod(x,10)) 
            x=int(x/10) 
            
            
            if(res>max//10 or (res==max//10 and rem>=max%10)):
                return 0
            if(res<min//10 or (res==min//10 and rem<=min%10)):
                return 0 
            
            res=(res*10)+rem 
            
        return res