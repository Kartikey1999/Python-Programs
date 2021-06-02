def add(a,b):
    result=a+b
    print(result)

def sub(a,b):
    result=a-b
    print(result)

def mul(a,b):
    result=a*b
    print(result)

def div(a,b):
    result=a/b
    print(result)

def mod(a,b):
    result=a%b
    print(result)
    

a=int(input("enter first num: "))    
b=int(input("enter sec num: "))
op=input("enter operator")

if op=="+":
    add(a,b)

if op=="-":
    sub(a,b)

if op=="*":
    mul(a,b)

if op=="/":
    div(a,b)

if op=="%":
    mod(a,b)