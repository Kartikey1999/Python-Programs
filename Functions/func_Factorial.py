def myFact(n):
    if n==1:
        return n
    else:
        return n*myFact(n-1)
num=int(input("enter: "))
print(myFact(num))            