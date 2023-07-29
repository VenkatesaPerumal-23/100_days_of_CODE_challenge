#factorial of a number 
#User function Template for python3


class Solution:
    def factorial(self,N):
        fact=1
        if(N==0):
            return 1 
        else:
            for i in range(N,0,-1):
                fact=fact*i 
            return fact


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))

# } Driver Code Ends




#fibonacci number 
class Solution(object):
    def fib(self, n):
        if(n==0):
            return 0 
        elif(n==1):
            return 1
        else:
            a=0 
            b=1 
            for i in range(2,n+1): 
             c=a+b 
             a=b 
             b=c 

            return c