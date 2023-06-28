t=int(input()) 
for i in range(t):
    n,m,k=map(int,input().split()) 
    result=m*k 
    if(result>=n):
        print("YES") 
        
    else:
        print("NO")
