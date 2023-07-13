t=int(input()) 
for i in range(t):
    base_salary=int(input()) 
    if(base_salary<1500):
        hra=base_salary*(10/100)
        da=base_salary*(90/100)  
    elif(base_salary>=1500):
        hra=500 
        da=base_salary*(98/100)   
        
    gross_salary=base_salary+hra+da 
    print(gross_salary)
        
    