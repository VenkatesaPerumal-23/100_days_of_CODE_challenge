class Solution:
    def printTriangle(self, N):
        ascii_val=65
        for i in range(1,N+1): 
            string=""
            for j in range(ascii_val,ascii_val+i): 
                string=string+chr(j) 
                
            print(string)
                
            
            

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