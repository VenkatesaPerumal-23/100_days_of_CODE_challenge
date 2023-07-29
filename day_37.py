#factorial using recursion

def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
fact=int(input())
print(factorial(fact))

#fibonacci using recursion

def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
fib=int(input())
print(fibonacci(fib))
