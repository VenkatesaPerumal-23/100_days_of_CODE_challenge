#pattern-1 

class Solution:
    def printTriangle(self, N):
       string=""
       for i in range(1, N+1):
           if(i==1):
               string=string+str(i)
               print(string)
           else:
               string=str(string) +" "+ str(i)
               print(string)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if _name_ == '_main_':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends 

#pattern-2

class Solution:
    def printTriangle(self, N):
        val=1
        for i in range(1, N+1):
            i=str(i)
            print((i+" ")*val)
            val+=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if _name_ == '_main_':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends 

#pattern-3 

class Solution:
    def printTriangle(self, N):
        for i in range(N,0,-1):
            print("* "*i)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if _name_ == '_main_':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends 


#pattern-4

class Solution:
    def printTriangle(self, N):
        for i in range(N,0,-1):
            string="" 
            for j in range(1,i+1):
                string=string+str(j)+" "
           
            print(string)
            
                #{ 
 # Driver Code Starts
#Initial Template for Python 3

if _name_ == '_main_':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends
