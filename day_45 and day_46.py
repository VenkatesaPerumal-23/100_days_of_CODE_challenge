#sum_of_all_divisors_of_N
class Solution:
    def sumOfDivisors(self, N):
        sum_factor=0
        for i in range(1,N+1):
            sum_factor=sum_factor+(N//i)*i 
        return sum_factor

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
# } Driver Code Ends 

#second largest element in array or list
class Solution:

	def print2largest(self,arr, n):
	    set_arr=set(arr) 
	    length=len(set_arr) 
	    if(length>1):
	        set_arr=list(set_arr)
	        set_arr.sort() 
	        return set_arr[-2]
	    else:
	        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends