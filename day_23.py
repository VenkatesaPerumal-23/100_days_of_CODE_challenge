t=int(input()) 
for i in range(t):
    list1=list(map(int,input().split())) 
    list1.remove(max(list1))
    print(max(list1))