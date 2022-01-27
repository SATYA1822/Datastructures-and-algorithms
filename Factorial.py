#Recursive function
def factorial(n):
    if(n>1):
        return n*factorial(n-1) #recursive function
    else:
        return 1
print(factorial(5))