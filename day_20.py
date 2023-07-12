t=int(input()) 
for i in range(t):
    i=int(input())
    if(i%10==0):
        print(int(i/10)) 
        
    elif(i%5==0):
        print(int((i/10)+1))
        
    else:
        print("-1")

