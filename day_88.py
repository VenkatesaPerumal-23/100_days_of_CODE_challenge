#Number of occurrence
class Solution:
   def count(self,arr, n, x):
	    first=-1 
	    second=-1
		low=0 
		high=n-1 
		while(low<=high):
		    mid=(low+high)//2 
		    if(arr[mid]==x):
		        first=mid 
		        high=mid-1 
		    elif(arr[mid]>x):
		        high=mid-1 
		    else:
		        low=mid+1 
		low=0 
		high=n-1 
	    while(low<=high):
		    mid=(low+high)//2 
		    if(arr[mid]==x):
		        second=mid 
		        low=mid+1 
		    elif(arr[mid]>x):
		        high=mid-1 
		    else:
		        low=mid+1 
		        
		if(first==-1 or second==-1):
		    return 0 
		else:
		    return second-first+1
