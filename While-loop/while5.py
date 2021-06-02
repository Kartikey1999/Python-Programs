n=int(input("enter a number"))

cnt=1
a=0
b=1
c=1

while cnt<=n:
    print(a)
    a,b,c=b,c,a+b+c
    cnt+=1
