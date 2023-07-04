t=int(input()) 
for i in range(t):
    a,b=input().split() 
    a=int(a) 
    b=int(b)
    val_a=(a/10)*100 
    val_b=(b/20)*100 
    if(val_a == val_b):
        print("ANY") 
        
    elif(val_a>val_b):
        print("FIRST") 
        
    elif(val_a<val_b):
        print("SECOND") 