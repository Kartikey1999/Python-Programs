n=int(input("enter: "))

for i in range(1,n+1):
    for j in range(1,2*n):
        if i==j or i+j==2*n:
            print("*",end='')
        else:
            print(" ",end='')
    print()   