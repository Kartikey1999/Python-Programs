n=int(input("enter: "))
mid=(n+1)//2
i=1
while i<=n:
    j=1
    while j<=n:
        if i==mid or j==mid or (i==1 and j>mid) or (j==n and i>mid) or (i==n and j<mid) or(j==1 and i<mid):
            print("*",end=' ')
        else:
            print(" ",end=' ')
        j+=1
    print()
    i+=1


   