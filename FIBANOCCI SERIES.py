n=int(input('number of terms:'))
n1=0
n2=1
i=0
if n<=0:
    print("enter a positive integer")
elif n==1:
    print("fibonacci series upto",n,":")
    print(n1)
else:
    print("fibanocci sequence:")
    while i<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        i=i+1
   
