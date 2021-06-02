n=int(input("enter a number"))

a=0
b=1
cnt=1

while cnt<=n:
    print(a)
    a,b=b,a+b
    cnt+=1