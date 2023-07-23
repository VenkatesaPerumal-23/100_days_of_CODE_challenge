#pattern-1

class Solution:
    def printTriangle(self, N):
        
        for i in range(N,0,-1):
            space=2*(N-i)
            string1="" 
            string2=""
           
            for j in range(i,0,-1):
                string1=string1+"*" 
                     
            for k in range(i,0,-1):
                string2=string2+"*" 
                    

            print(string1+" "*space+string2)  
                
                
        for i in range(1,N+1):
            space=2*(N-i) 
            string1="" 
            string2=""  
            
            for j in range(1,i+1):
                string1=string1+"*" 
                
            for k in range(1,i+1):
                string2=string2+"*"  
                
            print(string1+" "*space+string2) 
            
                
            
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

class Solution:
    def printTriangle(self, N):
        space=" "*(N-2) 
        for i in range(1,N+1):
            if(i==1 or i==N):
                print("*"*N) 
            else: 
                print("*"+space+"*")
                


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