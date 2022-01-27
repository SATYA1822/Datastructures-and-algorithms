def prime(n):
    flag=True #it is to take as boolean value
    if n>1:
        for i in range(2,n):
            if(n%i==0):
                flag=True

                break
    if flag:                               #it indirectly takes as true
        print("it is not  a prime number")
    else:
        print("it is a prime number")
prime(8)