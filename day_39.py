#Selection Sort

class Solution: 
    def select(self,arr, i):
        min_element=i 
        for j in range(i+1,len(arr)):
            if(arr[min_element]>arr[j]):
                min_element=j 
                
        return min_element
        
    def selectionSort(self,arr,n):
        for i in range(n):
            minn=self.select(arr,i) 
            arr[i],arr[minn]=arr[minn],arr[i] 

            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends