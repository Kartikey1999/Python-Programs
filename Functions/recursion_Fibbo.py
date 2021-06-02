def myFibbo(n):
    if n==0 or n==1:
        return n
    else:
        return myFibbo(n-1) + myFibbo(n-2)

n=int(input("enter: "))
print(myFibbo(n))
          
