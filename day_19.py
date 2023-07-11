t=int(input()) 
for i in range(t):
    n,m=map(int,input().split()) 
    if(n<m):
        print(n) 
    elif(m==0):
        print(2*n) 
        
    else:
        x=n-m 
        x=x+n 
        print(x)