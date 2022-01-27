#swapping without third variable
a=int(input("enter the value of a "))
b=int(input("enter the value of b "))
c=int(input("enter the value of c "))
d=int(input("enter the value of d "))
a=a+b
b=a-b
a=a-b
print("the value of a",a)
print("the value of b",b)
c=c^d #using xor because of not wasting bits
d=c^d
c=c^d
print("the value of c",c)
print("the value of d",d)

