#pattern-1
#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            string="* "*i 
            print(string) 
            
        N=N-1 
        for j in range(N,0,-1):
            string="* "*j 
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



#pattern-2
#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            if(i==1):
                print(i) 
                
            elif(i%2==0):
                string="0 1 "*(int(i/2)) 
                print(string)
                
                
            elif(i%2!=0): 
                string="1 "+"0 1 "*(int(i/2)) 
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