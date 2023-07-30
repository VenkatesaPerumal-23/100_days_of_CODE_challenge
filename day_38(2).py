#binary to decimal
class Solution:
     def binary_to_decimal(self, str):
     dec=int(str) 
     decimal=0
     p=0
     while(dec>0):
        rem=dec%10
        decimal=decimal+rem*pow(2,p)
        dec=int(dec/10)
        p+=1
     return decimal;


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution();
		ans = ob.binary_to_decimal(str)
		print(ans)
# } Driver Code Ends
