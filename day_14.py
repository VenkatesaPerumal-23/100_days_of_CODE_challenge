t=int(input()) 
for i in range(t):
    x,a,b=map(int,input().split()) 
    a*=1 
    b*=2 
    result=a+b 
    if(result>=x):
        print("Qualify") 
        
    else:
        print("NotQualify") 

    