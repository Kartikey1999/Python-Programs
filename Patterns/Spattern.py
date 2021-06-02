n=int(input("enter: "))
mid=(n+1)//2
i=1
while i<=n:
    j=1
    while j<=n:
        if i==1 or i==mid or i==n or (j==1 and mid>i) or (j==n and i>mid):
            print("*",end=' ')
        else:
            print(" ",end=' ')
        j+=1
    print()
    i+=1
