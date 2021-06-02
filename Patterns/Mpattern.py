n=int(input("enter: "))
mid=(n+1)//2
i=1
while i<=n:
    j=n 
    while j>=1:
        if j==1 or j==n or (i==j and i<=mid) or (i+j==n+1 and i<=mid) :
            print("*",end=' ')
        else:
            print(" ",end=' ')
        j-=1
    print()
    i+=1