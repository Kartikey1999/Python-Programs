a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))

if a>b:
    max=a
    smax=b
else:
    max=b
    smax=a
if c>max:
    smax=max
    max=c
elif c>smax:
    smax=c

print(smax)