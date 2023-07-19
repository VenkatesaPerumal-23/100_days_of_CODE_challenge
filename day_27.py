

#pattern-1

class Solution:
    def printTriangle(self, N):
        stars=1
        for i in range(1,N+1):
            string="" 
            space=N-i 
            string=string+(" "*space)+"*"*(stars) 
            print(string) 
            stars+=2


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends

#pattern-2

class Solution:
    def printTriangle(self, N):
        n=2*N-1
        for i in range(N):
            space=i 
            string=""
            for j in range(1,n+1):
                string=string+"*" 
            
            print(" "*(space)+string)
            n-=2
            
            
        
#{ 
 # Driver Code Starts

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends


#pattern-3

class Solution:
    def printDiamond(self, N):
        for i in range(1,N+1):
            string="" 
            space=N-i 
            string=string+(" "*space)+"* "*(i) 
            print(string)  
        for j in range(N,0,-1):
            string="" 
            space=N-j 
            string=string+"* "*j 
            print(" "*space+string)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printDiamond(N)
# } Driver Code Ends
