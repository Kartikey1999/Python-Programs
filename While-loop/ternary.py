a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
d=int(input("enter a number"))

max=a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d 
print(max)