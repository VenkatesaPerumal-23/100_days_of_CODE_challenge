t=int(input()) 
for i in range(t):
    n,m=map(int,input().split()) 
    total_tyres=2*(n) + 4*(m) 
    print(total_tyres)
