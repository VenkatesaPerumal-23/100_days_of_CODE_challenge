#Floor and Ceil
def getFloorAndCeil(arr, n, x):
    fl=floor(arr, n, x)
    ce=ceil(arr, n, x) 
    return (fl, ce)
   
def floor(arr, n, x):
    low=0 
    high=n-1 
    result=-1 
    arr.sort()
    while(low<=high):
        mid=(low+high)//2 
        if(arr[mid]<=x):
            result=arr[mid]
            low=mid+1
        else:
            high=mid-1
    return result
   
def ceil(arr, n, x):
    low=0 
    high=n-1 
    result=-1 
    arr.sort()
    while(low<=high):
        mid=(low+high)//2 
        if(arr[mid]>=x):
            result=arr[mid]
            high=mid-1 
        else:
            low=mid+1
    return result