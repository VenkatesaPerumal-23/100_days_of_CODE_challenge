#Find leaders in an array
class Solution:
   
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        result=[] 
        leader=A[-1] 
        result.append(leader)
        for i in range(N-2,-1,-1):
            if A[i]>=leader:
                leader=A[i] 
                result.append(leader) 
        result=reversed(result)
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends