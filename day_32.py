#User function Template for python3

class Solution:
    def printTriangle(self, N):
        start=0 
        k=2*N-1  
        end=k-1 
        num=N
        matrix=[[i for i in range(k)]for j in range(k)] 
        
        for i in range(N):
            for j in range(start,end+1):
                matrix[i][j]=num 
            for j in range(start+1,end+1):
                matrix[j][i]=num  
            for j in range(start+1,end+1):
                matrix[end][j]=num 
            for j in range(start+1,end):
                matrix[j][end]=num
                
            start+=1 
            end-=1 
            num-=1 
            
        for i in range(k):
            for j in range(k):
                print(matrix[i][j],end=" ") 
            print()
                
        
            
                    
            
                
                
                
       
            
           

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends