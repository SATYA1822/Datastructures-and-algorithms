def fibonacci(n):
   p=0
   q=1
   print(p)
   print(q)
   for i in range(2,n):
       r=p+q
       p=q
       q=r
       print(r)
fibonacci(4)