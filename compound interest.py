#Finding the compound interest

def CI(p,t,r):
    print("enter the principal amount", p)
    print("enter the time period ", t)
    print("enter the rate of interest", r)
    ci = p*((1+r)**1/t)
    return ci


print("THE COMPOUND INTEREST IS", CI(100, 5, 10))