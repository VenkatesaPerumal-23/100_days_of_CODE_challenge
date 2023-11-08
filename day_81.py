#inversionCount
def inversionCount(self, arr, n):
        count=0
        if(len(arr)>1):
            mid=len(arr)//2
            L=arr[:mid]
            R=arr[mid:]
            count+=self.inversionCount(L,len(L))
            count+=self.inversionCount(R,len(R))
            
            i=j=k=0
            while(i<len(L) and j<len(R)):
                if(L[i]<=R[j]):
                    arr[k]=L[i]
                    i+=1
                else:
                    arr[k]=R[j]
                    count+=len(L)-i
                    j+=1
                k+=1
            
            while(i<len(L)):
                arr[k]=L[i]
                i+=1
                k+=1
            while(j<len(R)):
                arr[k]=R[j]
                j+=1
                k+=1
        return count