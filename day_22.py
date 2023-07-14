t=int(input())
for i in range(t):
    n=int(input())  
    coeff=list(map(int,input().split()))
    length=len(coeff)-1
    list1=[]
    for num in range(length,-1,-1): 
        list1.append(coeff[num]) 
        
    for val in range(len(list1)):
        if(list1[val]!=0):
            print(n-val-1) 
            break
            
        else: 
            pass
            
        
            
