def mySwap(a,b):
    a,b=b,a
    return a,b
x=int(input("enter: "))    
y=int(input("enter: "))
print("before swap values ",x,y)
x,y=mySwap(x,y)
print("after swap values ",x,y)