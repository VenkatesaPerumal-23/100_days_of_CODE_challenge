#armstrong number
#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        temp=int(n) 
        rem=0 
        arm=0
        while(n>0):
            rem=n%10 
            arm=arm+(rem**3) 
            n=int(n/10) 
            
        if(temp==arm):
            return 'Yes' 
        else:
            return 'No'

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends




#palindrome
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
           return False 
        temp=x 
        reverse=0 
        rem=0
        while(x!=0):
            rem=x%10
            reverse=reverse*10 + rem
            x//=10
        return reverse==temp