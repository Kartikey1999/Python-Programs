n=int(input("enter: "))
i=1
while i<=n:
    j=n
    while j>=1:
        if i==1 or i==n or i==j:
            print("*",end=' ')
        else:
            print(' ',end=' ')
        j-=1
    print()
    i+=1            