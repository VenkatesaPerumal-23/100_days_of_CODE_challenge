# pattern-1
class Solution:
    def printTriangle(self, N):
        space=2*(2*N-2)
        for i in range(1,N+1): 
            string1="" 
            string2=""
            if(i==1):
                string1="1 "+" "*space+"1" 
                print(string1)  
                space-=4 
            
            elif(i==N): 
                for j in range(1,N+1):
                    string1=string1+str(j)+" "  
                for k in range(N,0,-1):
                    string2=string2+str(k)+" "
                     
                print(string1+string2)  
                
            else:
                for j in range(1,i+1):
                    string1=string1+str(j)+" " 
                for k in range(i,0,-1):
                    string2=string2+str(k)+" "
                     
                print(string1+" "*space+string2) 
                space-=4
                
                    
                    
                    
                

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

# pattern-2 

class Solution:
    def printTriangle(self, N):
        start=1
        for i in range(1,N+1):
            string="" 
            for j in range(start,start+i):
                string=string+str(j)+" " 
            print(string)  
            start=j+1 
                
                
                


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
